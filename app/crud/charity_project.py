from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.charity_project import CharityProject
from app.schemas.charity_project import (
    CharityProjectCreate,
    CharityProjectUpdate,
)
from .base import CRUDBase


class CRUDCharityProject(CRUDBase):
    """
    CRUD для CharityProject с проверкой уникальности имени.
    """

    async def _check_name_unique(
            self, session: AsyncSession, name: str
    ) -> None:
        """
        Проверяет, что проект с таким именем не существует.
        Если существует — бросает HTTPException.
        """
        result = await session.execute(
            select(CharityProject).where(CharityProject.name == name)
        )
        existing_project = result.scalar_one_or_none()
        if existing_project:
            raise HTTPException(
                status_code=400,
                detail="Проект с таким именем уже существует."
            )

    async def create(
        self,
        session: AsyncSession,
        obj_in: CharityProjectCreate,
    ) -> CharityProject:
        """
        Создает проект, проверяя уникальность имени.
        """
        await self._check_name_unique(session, obj_in.name)
        return await super().create(obj_in, session)

    async def update(
        self,
        session: AsyncSession,
        db_obj: CharityProject,
        obj_in: CharityProjectUpdate
    ) -> CharityProject:
        """
        Обновляет проект, проверяя уникальность нового имени.
        """
        if obj_in.name and obj_in.name != db_obj.name:
            await self._check_name_unique(session, obj_in.name)
        return await super().update(db_obj, obj_in, session)


crud_charityproject = CRUDCharityProject(CharityProject)
