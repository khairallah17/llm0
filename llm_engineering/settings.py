from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    LINKEDIN_USERNAME: str | None = None
    LINKEDIN_PASSOWRD: str | None = None

    DATABASE_NAME: str | None = None