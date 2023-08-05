from cnnClasifier.config.configuration import ConfigurationManager
from cnnClasifier.components.prepare_base_model import PrepareBaseModel
from cnnClasifier import logger

STAGE_NAME =  "Prepare Base Model"

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        # Init ConfigurationManager Class
        config = ConfigurationManager()
        # Calling get_prepare_base_model_config from ConfigurationManager Class
        prepare_base_model_config = config.get_prepare_base_model_config()
        # Calling PrepareBaseModel Component
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        # get_base_model function from PrepareBaseModel Class
        prepare_base_model.get_base_model()
        # update_base_model function from PrepareBaseModel Class
        prepare_base_model.update_base_model()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> Stage: {STAGE_NAME} started <<<<<<<")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>> Stage: {STAGE_NAME} completed <<<<<<<\n\nx========x")
    except Exception as e:
        raise e