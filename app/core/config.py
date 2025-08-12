from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    """
    Настройки приложения для благотворительного фонда.
    """

    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = 'Фонд собирает пожертвования.'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
