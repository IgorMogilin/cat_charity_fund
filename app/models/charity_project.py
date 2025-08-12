from sqlalchemy import Column, String, Text

from .base import BaseProjectModel


class CharityProject(BaseProjectModel):
    """Модель благотворительного проекта."""
    name = Column(
        String(100), nullable=False, unique=True
    )
    description = Column(
        Text, nullable=False
    )
