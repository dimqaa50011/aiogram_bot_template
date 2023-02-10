from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from .config import Settings

conf = Settings()

async_engine = create_async_engine(conf.db_conf.SQLALCHEMY_DATABASE_URI)
async_session = sessionmaker(bind=async_engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()
