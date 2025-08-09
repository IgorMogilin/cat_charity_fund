from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, PositiveInt, root_validator


class CharityProjectBase(BaseModel):
    name: str = Field(
        ..., min_length=1, max_length=100
    )
    description: str = Field(
        ..., min_length=1
    )
    full_amount: PositiveInt


class CharityProjectCreate(CharityProjectBase):
    pass


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(
        None, min_length=1, max_length=100
    )
    description: Optional[str] = Field(
        None, min_length=1
    )
    full_amount: Optional[PositiveInt] = None


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int = 0
    fully_invested: bool = False
    create_date: datetime
    closed_date: Optional[datetime] = None

    class Config:
        orm_mode = True