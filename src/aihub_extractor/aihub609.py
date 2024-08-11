import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub609:
    directory_name = "028.다국어_구어체_번역_병렬_말뭉치_데이터"

    info = {
        "확인일": "2024-08-12",
        "시리얼번호": 609,
        "이름": "다국어 구어체 번역 병렬 말뭉치 데이터",
        "구축년도": 2022,
        "용량": "564.49 MB",
        "버전": "1.0",
        "일자": "2022-07-29",
        "변경내용": "데이터 최종 개방",
        "데이터 구축량": 8_6000_000,
    }

    files = [
        "01.데이터/1_Training/라벨링데이터/TL1.zip",
        "01.데이터/2_Validation/라벨링데이터/VL1.zip",
    ]

    def __init__(self, data_dir=""):
        self.data_dir = data_dir

    @staticmethod
    def get_dataframe_from_xlsx(xlsx_path):
        return pd.read_excel(xlsx_path, engine="openpyxl")

    @staticmethod
    def get_records_from_zip(zip_path):
        all_records = []
        with zipfile.ZipFile(zip_path) as zip_file:
            for filename in zip_file.namelist():
                logger.info(filename)
                if not filename.endswith(".json"):
                    continue

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
            records = self.get_records_from_zip(file_path)
            all_records += records

        logger.info(len(all_records))
        return records


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    data_dir = "/home/ubuntu/AIHub/corpus/028.다국어_구어체_번역_병렬_말뭉치_데이터"
    extractor = AIHub609(data_dir)
    extractor.extract_as_records()
