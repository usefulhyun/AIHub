import json
import zipfile
import pandas as pd
import logging


logger = logging.getLogger(__name__)


class AIHub71720:
    directory_name = "113.국내_법률_대상_다국어_번역_데이터"

    info = {
        "확인일": "2024-08-14",
        "시리얼번호": 71720,
        "이름": "국내 법률 대상 다국어 번역 데이터",
        "구축년도": 2023,
        "용량": "559.10 MB",
        "버전": "1.0",
        "일자": "2024-06-28",
        "변경내용": "데이터 개방",
    }

    files = [
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_가사_친족법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_가사_친족법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_가사_친족법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_근로기준법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_근로기준법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_근로기준법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_부동산_관련_법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_부동산_관련_법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_부동산_관련_법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_일반민법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_일반민법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_민사_일반민법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_조세_종합소득세_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_조세_종합소득세_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_조세_종합소득세_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_근로기준법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_근로기준법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_특별형법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_특별형법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_특별형법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_형법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_형법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_형법_판결문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_형사소송법_결정문_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_형사소송법_조서_중국어(cn).zip",
        "3.개방데이터/1.데이터/Training/02.라벨링데이터/TL_형사_형사소송법_판결문_중국어(cn).zip",
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
                    # info Dataset Annotations
                    records = json.load(f_in)["Annotations"]
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

    data_dir = "/home/ubuntu/AIHub/corpus/113.국내_법률_대상_다국어_번역_데이터"
    extractor = AIHub71720(data_dir)
    extractor.extract_as_records()
