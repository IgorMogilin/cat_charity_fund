from datetime import datetime
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (
    check_full_amount_not_less_than_invested,
    check_project_can_be_deleted,
    check_project_exists,
    check_project_not_fully_invested,
)
from app.core.db import get_async_session
from app.core.dependencies import current_superuser
from app.crud.charity_project import crud_charityproject
from app.models import Donation, User
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectDB,
    CharityProjectUpdate,
)
from app.services.investments import invest_money


router = APIRouter()


@router.get(
    '/',
    response_model=List[CharityProjectDB],
    response_model_exclude_none=True
)
async def get_all_projects(
    session: AsyncSession = Depends(get_async_session)
):
    """Получить список всех благотворительных проектов."""
    return await crud_charityproject.get_multi(session)


@router.post(
    '/',
    response_model=CharityProjectDB,
    response_model_exclude_none=True
)
async def create_new_project(
    project_in: CharityProjectCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser)
):
    """
    Создать новый благотворительный проект.
    Автоматически распределяет доступные пожертвования.
    Только для суперпользователей.
    """
    new_project = await crud_charityproject.create(session, project_in)

    result = await session.execute(
        select(Donation)
        .where(Donation.fully_invested.is_(False))
        .order_by(Donation.create_date)
    )
    open_donations = result.scalars().all()
    changed_objs = invest_money(target=new_project, sources=open_donations)
    for obj in changed_objs:
        session.add(obj)
    await session.commit()
    await session.refresh(new_project)
    return new_project


@router.patch(
    '/{project_id}',
    response_model=CharityProjectDB,
    response_model_exclude_none=True
)
async def partially_update_project(
    project_id: int,
    project_in: CharityProjectUpdate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser)
):
    """
    Обновить информацию о проекте.
    Проверяет возможность изменения.
    Только для суперпользователей.
    """
    db_project = await crud_charityproject.get(project_id, session)
    check_project_exists(db_project)
    check_project_not_fully_invested(db_project)
    check_full_amount_not_less_than_invested(
        project_in.full_amount, db_project.invested_amount
    )
    project = await crud_charityproject.update(session, db_project, project_in)
    if project.full_amount == project.invested_amount:
        project.fully_invested = True
        project.close_date = datetime.utcnow()
        await session.commit()
        await session.refresh(project)
    return project


@router.delete(
    '/{project_id}',
    response_model=CharityProjectDB
)
async def delete_project(
    project_id: int,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser)
):
    """
    Удалить проект.
    Проверяет возможность удаления.
    Только для суперпользователей.
    """
    project = await crud_charityproject.get(project_id, session)
    check_project_exists(project)
    check_project_can_be_deleted(project)
    return await crud_charityproject.remove(project, session)
