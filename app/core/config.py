from dotenv import find_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings):
    model_config = SettingsConfigDict()

    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    DB_USER: str = "postgres"
    DB_PASS: str = "mypassword"
    DB_NAME: str = "my_db"
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    API_KEY: str

    @property
    def ASYNC_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

if os.path.exists('/.dockerenv'):
    settings = Settings()
else:
    settings = Settings(_env_file=find_dotenv())