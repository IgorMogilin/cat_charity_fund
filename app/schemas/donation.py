from datetime import datetime
from typing import Optional
from pydantic import BaseModel, PositiveInt


class DonationBase(BaseModel):
    full_amount: PositiveInt
    comment: Optional[str] = None


class DonationCreate(DonationBase):
    pass


class DonationDB(DonationBase):
    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationAdminDB(DonationDB):
    invested_amount: int
    fully_invested: bool
    user_id: int