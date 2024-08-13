import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71591:
    directory_name = "036.방송콘텐츠_한국어-아시아어_번역_말뭉치"

    info = {
        "시리얼번호": 71591,
        "이름": "방송콘텐츠 한국어-아시아어 번역 말뭉치",
        "구축년도": 2022,
        "용량": "2.99 GB",
        "버전": "1.1",
        "일자": "2024-01-10",
        "변경내용": "데이터 최종 개방",
        "데이터 구축량": 2_500_000,
    }

    files = [
        "01-1.정식개방데이터/Training/02.라벨링데이터/TL.zip",
        "01-1.정식개방데이터/Validation/02.라벨링데이터/VL.zip",
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
                if not filename.endswith(".json"):
                    continue
                try:
                    with zip_file.open(filename, "rb") as f_in:
                        records = [json.load(f_in)]
                        all_records += records

                        # logger.info(zip_path)
                        # logger.info(filename)
                        # logger.info(records[0])
                        # logger.info(records[0].keys())
                        # logger.info(len(records))
                except:
                    logger.info(filename)
                    # with zip_file.open(filename) as f_in:
                    #    logger.info(f_in.read())

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

    data_dir = "/home/ubuntu/AIHub/corpus/036.방송콘텐츠_한국어-아시아어_번역_말뭉치"
    extractor = AIHub71591(data_dir)
    extractor.extract_as_records()
