from cnnClasifier.config.configuration import ConfigurationManager
from cnnClasifier.components.data_ingestion import DataIngestion
from cnnClasifier import logger

STAGE_NAME =  "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Init ConfigurationManager Class
        config = ConfigurationManager()
        # Calling get_data_ingestion_config from ConfigurationManager Class
        data_ingestion_config = config.get_data_ingestion_config()
        # Calling DataIngestion Component
        data_ingestion = DataIngestion(config=data_ingestion_config)
        # download_file function from DataIngestion Class
        data_ingestion.download_file()
        # extract_zip_file function from DataIngestion Class
        data_ingestion.extract_zip_file()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> Stage: {STAGE_NAME} started <<<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx========x")
    except Exception as e:
        raise e