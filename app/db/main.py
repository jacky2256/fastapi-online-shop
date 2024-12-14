import asyncio
from sqlmodel import create_engine, text, SQLModel
from sqlalchemy.ext.asyncio import AsyncEngine
from app.config import Config

engine = AsyncEngine(
create_engine(
    url=Config.DATABASE_URL,
    echo=True,
    pool_size=5,
    max_overflow=10,
))

async def init_db():
    async with engine.connect() as conn:
        from app.datanyze.models import *
        await conn.run_sync( SQLModel.metadata.create_all)

if __name__ == "__main__":
    asyncio.run(init_db())
