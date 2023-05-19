from fastapi_users import FastAPIUsers
from fastapi_users.authentication import (AuthenticationBackend,
CookieTransport, JWTStrategy)
from dotenv import load_dotenv
from os import environ


load_dotenv()
POSTGRES_HOST = environ.get("POSTGRES_HOST")
POSTGRES_DB = environ.get("POSTGRES_DB")
POSTGRES_USER = environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = environ.get("POSTGRES_PASSWORD")
POSTGRES_PORT = environ.get("POSTGRES_PORT")
SECRET_AUTH = environ.get("SECRET_AUTH")
POSTGRES_DB_TEST = environ.get("POSTGRES_DB_TEST")
DATABASE_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

DATABASE_URL_TEST = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
