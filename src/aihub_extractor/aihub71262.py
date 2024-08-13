import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71262:
    directory_name = "156.전문분야_영-한,_중-한_번역_말뭉치(식품)"

    info = {
        "확인일": "2024-08-12",
        "시리얼번호": 71262,
        "이름": "전문분야 영-한·중-한 번역 말뭉치 (식품)",
        "구축년도": 2021,
        "용량": "1.05 GB",
        "버전": "1.0",
        "일자": "2022-07-29",
        "변경내용": "데이터 최초 개방",
        "데이터 구축량": "300만 문장",
    }

    files = [
        "01.데이터/1.Training/라벨링데이터/TL1.zip",
        "01.데이터/1.Training/라벨링데이터/TL2.zip",
        "01.데이터/2.Validation/라벨링데이터/VL1.zip",
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
                    records = json.load(f_in)["data"]
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

    data_dir = "/home/ubuntu/AIHub/corpus/156.전문분야_영-한,_중-한_번역_말뭉치(식품)"
    extractor = AIHub71262(data_dir)
    extractor.extract_as_records()
