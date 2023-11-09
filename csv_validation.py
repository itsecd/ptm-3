import pandas as pd
import re
from typing import List
from checksum import calculate_checksum, serialize_result


VALIDATION_RULES = {
    'email': r'[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}',
    'height': r'\d\.\d{2}',
    'inn': r'\d{12}',
    'passport': r'\d{2}\s\d{2}\s\d{6}',
    'occupation': r'[\wа-яА-ЯёЁ-]+(\s[\wа-яА-ЯёЁ-]+)*',
    'latitude': r'-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?)',
    'hex_color': r'#([a-f0-9]{6}|[a-f0-9]{3})',
    'issn': r'\d{4}-\d{4}',
    'uuid': r'[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}',
    'time': r'([01]?\d|2[0-3]):([0-5]?\d):([0-5]?\d)(\.\d{1,6})?'
}
FILE_PATH = '23.csv'


def validate_csv(file_path: str, validation_rules: dict[str]) -> List[int]:
    """
     Validate rows in csv file. This function is used to validate csv rows by regex. It will return list of invalid rows
     
     :param file_path - path of csv file to be validated
     :param validation_rules - list of regex for validation. It is expected to contain column and regex
     
     :return list of invalid rows
    """
    invalid_rows_list = []
    try:
        df = pd.read_csv(file_path, sep=';', quotechar='"', encoding='utf-16')
        for index, row in df.iterrows():
            for column, regex in validation_rules.items():
                if not re.fullmatch(regex, str(row[column])):
                    invalid_rows_list.append(index)
                    break
    except Exception as e:
        print(f'Произошла ошибка при чтении файла: {e}')
    
    return invalid_rows_list
    

if __name__ == '__main__':
    invalid_list = validate_csv(FILE_PATH, VALIDATION_RULES)

    checksum = calculate_checksum(invalid_list)
    serialize_result(variant=23, checksum=checksum)
    