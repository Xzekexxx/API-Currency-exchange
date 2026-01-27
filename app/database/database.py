from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

from app.core.config import settings

from app.database.base import Base

engine = create_async_engine(settings.ASYNC_DATABASE_URL)

async_sessionmaker = async_sessionmaker(engine, class_=AsyncSession)

async def get_session():
    async with async_sessionmaker() as db:
        yield db
