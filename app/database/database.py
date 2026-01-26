from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from app.core.config import settings

engine = create_async_engine(settings.ASYNC_DATABASE_URL)

async_sessionmaker = async_sessionmaker(engine, class_=AsyncSession)

async def get_session():
    async with async_sessionmaker() as db:
        yield db

class Base(DeclarativeBase):
    pass