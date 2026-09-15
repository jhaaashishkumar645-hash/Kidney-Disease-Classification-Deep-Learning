import os
import zipfile
import gdown
from cnnClassifier import logger


class DataIngestion:

    def __init__(self, config):
        self.config = config

    def download_file(self) -> str:
        try:
            zip_download_path = self.config.local_data_file

            os.makedirs(os.path.dirname(zip_download_path), exist_ok=True)

            # If dataset already exists, skip downloading
            if os.path.exists(zip_download_path):
                logger.info(
                    f"Dataset already exists at: [{zip_download_path}]. "
                    "Skipping download."
                )
                return str(zip_download_path)

            dataset_url = self.config.source_URL

            logger.info(
                f"Downloading file from: [{dataset_url}] "
                f"into file: [{zip_download_path}]"
            )

            gdown.download(
                dataset_url,
                zip_download_path,
                quiet=False
            )

            logger.info(
                f"Downloaded file successfully to: [{zip_download_path}]"
            )

            return str(zip_download_path)

        except Exception as e:
            raise e

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)

        logger.info(
            f"Extracting zip file: [{self.config.local_data_file}]"
        )

        with zipfile.ZipFile(
            self.config.local_data_file,
            "r"
        ) as zip_ref:
            zip_ref.extractall(unzip_path)

        logger.info(
            f"Zip file extracted successfully to: [{unzip_path}]"
        )