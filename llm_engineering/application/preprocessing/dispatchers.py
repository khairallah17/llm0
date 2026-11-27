from loguru import get_logger

from.cleaning_data_handlers import (
    CleaningDataHandler,
    PostCleaningHandler,
    ArticleCleaningHandler,
    RepositoryCleaningHandler
)
from llm_engineering.domain.documents import NoSQLBaseDocument
from llm_engineering.domain.base.vector import VectorBaseDocument
from llm_engineering.domain.types import DataCategory

logger = get_logger(__name__)

class CleaningDispatcher:

    cleaning_factory = CleaningHandlerFactory()

    @classmethod
    def dispatch(cls, data_model: NoSQLBaseDocument) -> VectorBaseDocument:
        data_category = DataCategory(data_model.get_collection_name())
        handler = cls.cleaning_factory.create_handler(data_category)
        clean_model = handler.clean(data_model)

        logger.info(
            "Data cleaned successfully",
            data_category=data_category,
            cleaned_content_len=len(clean_model.conten)
        )

        return clean_model

class CleaningHandlerFactory():

    @staticmethod
    def create_handler(data_category: DataCategory) -> CleaningDataHandler:
        if data_category == DataCategory.POSTS:
            return PostCleaningHandler()
        elif data_category == DataCategory.ARTICLES:
            return ArticleCleaningHandler()
        elif data_category == DataCategory.REPOSITORIES:
            return RepositoryCleaningHandler()
        else:
            raise ValueError("Unsupported data type")
