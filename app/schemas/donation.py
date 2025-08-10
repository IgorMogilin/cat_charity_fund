from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str] = None


class DonationCreate(BaseModel):
    pass


class DonationDB(BaseModel):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationAdminDB(BaseModel):
    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime] = None

    class Config:
        orm_mode = True
