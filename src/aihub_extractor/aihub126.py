import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub126:
    directory_name = "12.한영말뭉치"

    info = {
        "버전": 1.0,
        "일자": "2019-12-31",
    }

    files = [
        "1_구어체(1)_200226.xlsx",
        "1_구어체(2)_200226.xlsx",
        "2_대화체_200226.xlsx",
        "3_문어체_뉴스(1)_200226.zip",
        "3_문어체_뉴스(2)_200226.xlsx",
        "3_문어체_뉴스(3)_200226.xlsx",
        "3_문어체_뉴스(4)_200226.xlsx",
        "4_문어체_한국문화_200226.xlsx",
        "5_문어체_조례_200226.xlsx",
        "6_문어체_지자체웹사이트_200226.xlsx",
    ]

    def __init__(self, data_dir=""):
        self.data_dir = data_dir

    @staticmethod
    def get_dataframe_from_xlsx(xlsx_path):
        return pd.read_excel(xlsx_path, engine="openpyxl")

    @staticmethod
    def get_dataframe_from_zip(zip_path):
        with zipfile.ZipFile(zip_path) as zip_file:
            assert len(zip_file.namelist()) == 1
            filename = zip_file.namelist()[0]
            with zip_file.open(filename) as f_in:
                dataframe = pd.read_excel(f_in)
        return dataframe

    def extract_as_records(self):
        all_records = []
        for file in self.files:
            file_path = f"{self.data_dir}/{file}"
            if file_path.endswith(".xlsx"):
                dataframe = self.get_dataframe_from_xlsx(file_path)
                records = dataframe.to_dict("records")
                all_records += records

            elif file_path.endswith(".zip"):
                dataframe = self.get_dataframe_from_zip(file_path)
                records = dataframe.to_dict("records")
                all_records += records
            else:
                assert False

            logger.info(file_path)
            logger.info(records[0])
            logger.info(records[0].keys())
            logger.info(len(records))

        logger.info(len(all_records))
        return records
