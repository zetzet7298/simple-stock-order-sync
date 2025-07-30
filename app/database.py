from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

# Tạo async engine
engine = create_async_engine(settings.database_url)

# Tạo async session factory
AsyncSessionLocal = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


class Base(DeclarativeBase):
    pass


# Dependency mới để lấy async session
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session
