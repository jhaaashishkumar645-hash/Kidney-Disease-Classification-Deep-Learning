from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline


STAGE_NAME = "Data Ingestion Stage"


try:
    logger.info(f">>>>> stage {STAGE_NAME} started <<<<<")

    obj = DataIngestionPipeline()
    obj.main()

    logger.info(
        f">>>>> stage {STAGE_NAME} completed! <<<<<\n\nx==========x"
    )

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare Base Model Stage"

try:
    logger.info(f"***** stage {STAGE_NAME} started <<<<<")
    
    prepare_base_model_ = PrepareBaseModelPipeline()
    prepare_base_model_.main()
    
    logger.info(f">>>>> stage {STAGE_NAME} completed! <<<<<\n\nx==========x")

except Exception as e:
    raise e