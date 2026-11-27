from loguru import logger
from pydantic_settings import BaseSettings, SettingsConfigDict
from zenml.client import Client
from zenml.exceptions import EntityExistsError

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    LINKEDIN_USERNAME: str | None = None
    LINKEDIN_PASSWORD: str | None = None

    DATABASE_NAME: str = "llmdb"
    DATABASE_HOST: str = "localhost"

    # RAG
    TEXT_EMBEDDING_MODEL_ID: str = "sentence-transformers/all-MiniLM-L6-v2"
    RERANKING_CROSS_ENCODER_MODEL_ID: str = "cross-encoder/ms-macro-MiniLM-L4-v2"
    RAG_MODEL_DEVICE: str = "cpu"

    #Qdrant Vector DB
    USE_QDRANT_CLOUD: bool = False
    QDRANT_DATABASE_HOST: str = "localhost"
    QDRANT_DATABASE_PORT: int = 6333
    QDRANT_CLOUD_URL: str | None = None
    QDRANT_APIKEY: str | None = None

    @classmethod
    def load_settings(cls) -> "Settings":

        try:
            logger.info("Loading settings from the ZenMl secret store.")

            settings_secrets = Client().get_secret("settings")
            settings = Settings(**settings_secrets.secret_values)

        except(RuntimeError, KeyError):

            logger.warning(
                "Failed to load settings from the ZenML secret store. Defaulting to loading the settings from the '.env' file"
            )

            settings = Settings()

        return settings

settings = Settings.load_settings()