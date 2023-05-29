import asyncio
from typing import AsyncGenerator
import pytest
from models.auth import User
from httpx import AsyncClient
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from dependencies import get_async_session, Base
from config import DATABASE_URL_TEST
from main import app
from alembic.config import Config
from alembic import command


alembic_cfg = Config("./alembic.ini")
engine_test = create_async_engine(DATABASE_URL_TEST, poolclass=NullPool)
async_session_maker = sessionmaker(engine_test, class_=AsyncSession, expire_on_commit=False)
Base.metadata.bind = engine_test

async def override_get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

app.dependency_overrides[get_async_session] = override_get_async_session

@pytest.fixture(autouse=True, scope='session')
async def prepare_database():
    command.upgrade(alembic_cfg, "head")
    yield
    session = async_session_maker()
    await session.execute(delete(User))
    await session.commit()
    await session.close()


@pytest.fixture(scope='session')
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()



@pytest.fixture(scope="module")
async def ac():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        yield ac
