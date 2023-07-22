"""
Settings module 
"""
from pydantic_settings import BaseSettings
from pathlib import Path

class APISettings(BaseSettings):
    API_VERSION: str = "1.0.0"
    API_DESCRIPTION: str = "API for the project"
    API_HOST: str = "localhost"
    API_PORT: int = 8000
    
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    class Config:
        env_file = ".env"
