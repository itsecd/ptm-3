import logging
import re
import pandas as pd
import checksum
from typing import  List

CSV_FILE = '62.csv'


def find_invalid_entries(dataframe: pd.DataFrame, column: str, reg_exp: str) -> List[int]:
    pass


if __name__ == '__main__':
    dataset = pd.read_csv(CSV_FILE, sep=';', quotechar='"', encoding='utf-16')
    print(dataset)
