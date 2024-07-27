from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine as _create_async_engine
from sqlalchemy.orm import sessionmaker

from exchange.settings import configuration


async_engine: AsyncEngine = _create_async_engine(
    url=configuration.db.DATABASE_URL_STRING,
    echo=True,
    pool_pre_ping=True
)


AsyncSessionLocal = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


@asynccontextmanager
async def Transaction():
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()

        except Exception:
            await session.rollback()
            raise

        finally:
            await session.close()
