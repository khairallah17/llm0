from zenml import pipeline, step
from zenml.logger import get_logger

logger = get_logger(__name__)

@step
def say_hello():
    logger.info("Excuting hello step")
    return "Hello World!"

@pipeline
def hello_pipeline():
    say_hello()