from sqlalchemy import Column, ForeignKey, Integer, Text

from .base import BaseProjectModel


class Donation(BaseProjectModel):
    user_id = Column(
        Integer, ForeignKey('user.id')
    )
    comment = Column(
        Text, nullable=True
    )
