from cnnClasifier import logger
from cnnClasifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClasifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME =  "Data Ingestion Stage"
try:
    logger.info(f">>>>>>> Stage: {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    raise e



STAGE_NAME =  "Prepare Base Model"

try:
    logger.info("*********************")
    logger.info(f">>>>>>> Stage: {STAGE_NAME} started <<<<<<<")
    prepare_baase_model = PrepareBaseModelTrainingPipeline()
    prepare_baase_model.main()
    logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    raise e