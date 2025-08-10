from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.user import current_superuser, current_user
from app.crud.donations import donation_crud
from app.models.user import User
from app.schemas.donation import DonationAdminDB, DonationCreate, DonationDB

router = APIRouter()


@router.post('/', response_model=DonationDB)
async def create_new_donation(
    donation: DonationCreate,
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_user)
):
    """Создать пожертвование."""
    return await donation_crud.create_donation(donation, session, user)


@router.get('/my', response_model=List[DonationDB])
async def read_my_donations(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """Получить пожертвования."""
    return await donation_crud.get_user_donations(session, user)


@router.get('/', response_model=List[DonationAdminDB])
async def read_all_donations(
    session: AsyncSession = Depends(get_async_session),
    user: User = Depends(current_superuser),
):
    """Получить все пожертвования."""
    return await donation_crud.get_all_donations(session)
