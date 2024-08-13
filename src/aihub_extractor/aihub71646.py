import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71646:
    directory_name = "008.다국어_번역_품질_평가_데이터"

    info = {
        "확인일": "2024-08-14",
        "시리얼번호": 71646,
        "이름": "다국어 번역 품질 평가 데이터",
        "구축년도": 2023,
        "용량": "111.76 MB",
        "버전": "1.0",
        "일자": "2024-08-06",
        "변경내용": "데이터 개방",
    }

    files = [
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_중-한_경제.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_중-한_과학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_중-한_문화.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_중-한_사회.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_중-한_정치.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_공학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_구어체.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_농수해양학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_복합학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_사회과학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_예술체육.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_의약학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_인문학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_번역말뭉치(HT)_한-중_자연과학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_중-한_경제.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_중-한_과학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_중-한_문화.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_중-한_사회.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_중-한_정치.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_공학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_구어체.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_농수해양학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_복합학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_사회과학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_예술체육.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_의약학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_인문학.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_평가데이터(MTPE)_한-중_자연과학.zip",
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

    data_dir = "/home/ubuntu/AIHub/corpus/008.다국어_번역_품질_평가_데이터"
    extractor = AIHub71646(data_dir)
    extractor.extract_as_records()
