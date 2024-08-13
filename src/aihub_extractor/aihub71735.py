import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71735:
    directory_name = "118.한-중,한-일_특허_및_기술과학_분야_병렬_말뭉치_데이터"

    info = {
        "확인일": "2024-08-14",
        "시리얼번호": 71735,
        "이름": "한-중/한-일 특허 및 기술과학 분야 병렬 말뭉치 데이터",
        "구축년도": 2023,
        "용량": "1.75 GB",
        "버전": "1.0",
        "일자": "2024-06-28",
        "변경내용": "데이터 개방",
        "데이터 구축량": "2,500,000",
    }

    files = [
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_011.특허_0111.B_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_011.특허_0112.C_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_011.특허_0113.F_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_011.특허_0114.G_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_011.특허_0115.H_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0121.EA.기계_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0122.ED.전기전자_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0123.EE.정보통신_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0124.EF.에너지자원_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0125.EG.원자력_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0126.LA.생명과학_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0127.NA.수학_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_01.한국특허_012.과학기술_0128.NB.물리학_kozh.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_021.특허_0211.B_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_021.특허_0212.C_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_021.특허_0213.F_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_021.특허_0214.G_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_021.특허_0215.H_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0221.EA.기계_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0222.ED.전기전자_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0223.EE.정보통신_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0224.EF.에너지자원_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0225.EG.원자력_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0226.LA.생명과학_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0227.NA.수학_zhko.zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_02.중국특허_022.과학기술_0228.NB.물리학_zhko.zip",
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

    data_dir = "/home/ubuntu/AIHub/corpus/118.한-중,한-일_특허_및_기술과학_분야_병렬_말뭉치_데이터"
    extractor = AIHub71735(data_dir)
    extractor.extract_as_records()
