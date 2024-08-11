import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71593:
    directory_name = "308.AI_허브_데이터_활용을_위한_기계_번역앱_구축과_번역기_평가_및_신규_말뭉치_구축"

    info = {
        "시리얼번호": 71593,
        "이름": "AI 허브 데이터 활용을 위한 기계 번역앱 구축과 번역기 평가 및 신규 말뭉치 구축",
        "구축년도": 2022,
        "용량": "618.33 MB",
        "버전": "1.1",
        "일자": "2023-12-15",
        "변경내용": "데이터 최종 개방",
        "데이터 구축량": 1_090_000,
    }

    files = [
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_01_AIHUB_데이터.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_02_용어사전.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_03_NER_태깅.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_04_신규구축_데이터_한영.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_04_신규구축_데이터_한일.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_04_신규구축_데이터_한중.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_05_번역기_평가_데이터_한영.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_05_번역기_평가_데이터_한일.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_05_번역기_평가_데이터_한중.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_06_유사문장_데이터_한영.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_06_유사문장_데이터_한일.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_06_유사문장_데이터_한중.zip",
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL_07_MTPE_시험_데이터.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_01_AIHUB_데이터.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_02_용어사전.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_03_NER_태깅.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_04_신규구축_데이터_한영.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_04_신규구축_데이터_한일.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_04_신규구축_데이터_한중.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_05_번역기_평가_데이터_한영.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_05_번역기_평가_데이터_한일.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_05_번역기_평가_데이터_한중.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_06_유사문장_데이터_한영.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_06_유사문장_데이터_한일.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_06_유사문장_데이터_한중.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL_07_MTPE_시험_데이터.zip",
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

    data_dir = "/home/ubuntu/AIHub/corpus/308.AI_허브_데이터_활용을_위한_기계_번역앱_구축과_번역기_평가_및_신규_말뭉치_구축"
    extractor = AIHub71593(data_dir)
    extractor.extract_as_records()
