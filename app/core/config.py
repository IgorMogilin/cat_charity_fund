from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = 'Фонд собирает пожертвования.'
    database_url: str = 'sqlite+aiosqlite:///:memory:'
    secret: str
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    PASSWORD_MIN_LENGTH: int = 3
    MIN_INVESTED_AMOUNT: int = 0

    class Config:
        env_file = '.env'


settings = Settings()
