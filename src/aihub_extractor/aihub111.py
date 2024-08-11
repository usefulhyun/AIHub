import json
import zipfile
import logging


logger = logging.getLogger(__name__)


class AIHub111:
    corpus_name = "전문분야 한영 말뭉치"
    directory_name = "006.전문분야한영"
    info = {"버전": "1.0", "일자": "2021-06-18"}

    files = [
        "1.Training/라벨링데이터/ko2en_training_json.zip",
        "2.Validation/라벨링데이터/ko2en_validation_json.zip",
    ]

    def __init__(self, data_dir=""):
        self.data_dir = data_dir

    @staticmethod
    def get_records_from_zip(zip_path):
        all_records = []
        with zipfile.ZipFile(zip_path) as zip_file:
            for filename in zip_file.namelist():
                with zip_file.open(filename) as f_in:
                    records = json.load(f_in)
                    all_records += records

                    logger.info(zip_path)
                    logger.info(filename)
                    logger.info(records[0])
                    logger.info(records[0].keys())
                    logger.info(len(records))

        return all_records

    def extract_as_records(self):
        all_records = []
        for file in self.files:
            file_path = f"{self.data_dir}/{file}"
            assert file_path.endswith(".zip")
            records = self.get_records_from_zip(file_path)
            all_records += records

        logger.info(len(all_records))
        return records
