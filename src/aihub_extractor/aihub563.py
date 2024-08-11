import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub563:
    directory_name = "155.산업정보_연계_주요국_특허_영-한_데이터"

    info = {
        "확인일": "2024-08-12",
        "시리얼번호": 563,
        "이름": "산업정보 연계 주요국 특허 영-한 데이터",
        "구축년도": 2021,
        "용량": "2.09 GB",
        "버전": "1.2",
        "일자": "2022-12-01",
        "변경내용": "라벨링데이터 수정",
        "데이터 구축량": "40만건",
    }

    files = [
        "01.데이터/1.Training/라벨링데이터_0831_add/TL_1.zip",
        "01.데이터/1.Training/라벨링데이터_0831_add/TL_2.zip",
        "01.데이터/1.Training/라벨링데이터_0831_add/TL_3.zip",
        "01.데이터/1.Training/라벨링데이터_0831_add/TL_4.zip",
        "01.데이터/1.Training/라벨링데이터_0831_add/TL_5.zip",
        "01.데이터/2.Validation/라벨링데이터_0831_add/VL_1.zip",
        "01.데이터/2.Validation/라벨링데이터_0831_add/VL_2.zip",
        "01.데이터/2.Validation/라벨링데이터_0831_add/VL_3.zip",
        "01.데이터/2.Validation/라벨링데이터_0831_add/VL_4.zip",
        "01.데이터/2.Validation/라벨링데이터_0831_add/VL_5.zip",
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
                    records = json.load(f_in)["labeled_data"]
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

    data_dir = "/home/ubuntu/AIHub/corpus/155.산업정보_연계_주요국_특허_영-한_데이터"
    extractor = AIHub563(data_dir)
    extractor.extract_as_records()
