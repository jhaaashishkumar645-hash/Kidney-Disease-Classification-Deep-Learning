from pathlib import Path

from cnnClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from cnnClassifier.utils.common import read_yaml
from cnnClassifier.entity.config_entity import (
    DataIngestionConfig,
    PrepareBaseModelConfig
)


class ConfigurationManager:

    def __init__(
        self,
        config_file_path=CONFIG_FILE_PATH,
        params_file_path=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

    def get_data_ingestion_config(self) -> DataIngestionConfig:

        config = self.config.data_ingestion

        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(config.root_dir),
            source_URL=config.source_URL,
            local_data_file=Path(config.local_data_file),
            unzip_dir=Path(config.unzip_dir)
        )

        return data_ingestion_config

    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:

        config = self.config.prepare_base_model

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_weights=self.params.WEIGHTS,
            params_include_top=self.params.INCLUDE_TOP,
            params_classes=self.params.CLASSES,
            params_learning_rate=self.params.LEARNING_RATE
        )

        return prepare_base_model_config