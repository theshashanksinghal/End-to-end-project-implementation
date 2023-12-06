from cnnClassifier import logger # we are able to import logger like this easily without doing cnnClassifier.logs.loggin blah blah only because we wrote logging code inside __init__.py
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started くくくくく")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} comp1eted くくくくくく\n\nx============x")
except Exception as e:
    logger.exception(e)
    raise e