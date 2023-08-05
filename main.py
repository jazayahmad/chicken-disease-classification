from cnnClasifier import logger
from cnnClasifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME =  "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage: {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    raise e