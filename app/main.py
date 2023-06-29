from fastapi import  FastAPI
from auth_config import auth_backend, fastapi_users
from schemas.auth import UserCreate, UserRead

app = FastAPI(
    title="Auth"
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth"],
)


