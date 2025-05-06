from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BookClub API"
    VERSION: str = "1.0.0"

    BACKEND_CORS_ORIGINS: list[str] = ["*"]

    SECRET_KEY: str = "super-secret-key"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7일

    SQLALCHEMY_DATABASE_URI: str = "sqlite:///./bookclub.db"

    class Config:
        env_file = ".env"

settings = Settings()
