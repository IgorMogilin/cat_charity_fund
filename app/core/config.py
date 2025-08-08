from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = 'Фонд собирает пожертвования.'
    database_url: str
    secret: str

    class Config:
        env_file = '.env'


settings = Settings()
