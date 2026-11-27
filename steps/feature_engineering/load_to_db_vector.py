from llm_engineering.application import utils

from typing import Annotated
from loguru import get_logger

from zenml import step

from llm_engineering.domain.base.vector import VectorBaseDocument

logger = get_logger(__name__)

@step
def load_to_db_vector(
    documents: Annotated[list, "documents"]
) -> None:
    logger.info(f"Loading {len(documents)} documents into the vectore database.")

    grouped_documents = VectorBaseDocument.group_by_class(documents)

    for document_class, documents in grouped_documents.items():
        logger.info(f"Loading documents into {document_class.get_collection_name()}")

        for documents_batch in utils.misc.batch(documents, size=4):

            try:
                document_class.bulk_insert(documents_batch)
            except Exception:
                return False

    return True