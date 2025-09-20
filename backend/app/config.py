from pydantic import BaseSettings
import os
class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@db:5432/ecommerce")
    JWT_SECRET: str = os.getenv("JWT_SECRET", "change_this_secret")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60*24*7
    ALGORITHM: str = "HS256"
settings = Settings()
