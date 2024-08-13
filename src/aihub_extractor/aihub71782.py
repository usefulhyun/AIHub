import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71782:
    directory_name = "116.금융_분야_다국어_병렬_말뭉치_데이터"

    info = {
        "시리얼번호": 71782,
        "이름": "금융 분야 다국어 병렬 말뭉치 데이터",
        "구축년도": 2023,
        "용량": "16.10 GB",
        "버전": "1.0",
        "일자": "2024-06-28",
        "변경내용": "데이터 개방",
    }

    files = [
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_1._학술논문_2._중국어간체.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_2._규제정보_2._중국어간체.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_3._보고서_2._중국어간체.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_4._뉴스기사_2._중국어간체.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_5._공시정보_2._중국어간체.zip",
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
                with zip_file.open(filename) as f_in:
                    records = json.load(f_in)["sents"]  # meta, doc_info, sents
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

    data_dir = "/home/ubuntu/AIHub/corpus/116.금융_분야_다국어_병렬_말뭉치_데이터"
    extractor = AIHub71782(data_dir)
    extractor.extract_as_records()
