import pytest
import pytest
from httpx import AsyncClient


async def test_register(ac: AsyncClient):
    response = await ac.post("/auth/register", json={
        "email": "user@example.com",
        "password": "string",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "string"
    })

    assert response.status_code == 201


#Тест на аутентификацию в процессе, артем разрешил сделать пр сейчас