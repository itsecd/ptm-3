import re
from pandas import pd
from checksum import calculate_checksum, serialize_result

VALIDATION_RULES = {
    'email_regex' : r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$',
    'height_regex' : r'^\d+(\.\d+)?$',
    'snils_regex': r'^\d{11}$',
    'passport_regex': r'^\d{2}\s\d{2}\s\d{6}$',
    'occupation_regex': r'^[А-Яа-я\s]+$',
    'longitude_regex': r'^-?\d+(\.\d+)?$',
    'hex_color_regex': r'^#[0-9A-Fa-f]{6}$',
    'issn_regex': r'^\d{4}-\d{4}$',
    'locale_code_regex': r'^[a-z]{2}-[a-z]{2}$',
    'time_regex': r'^\d{2}:\d{2}:\d{2}\.\d{6}$'
}
FILE_PATH = '35.csv'

def validate_csv(file_path: str, validation_rules: dict[str]) -> List[int]:
    """
     Проверка строк в csv-файле. Эта функция используется для проверки строк csv с помощью регулярного выражения. Она вернет список недопустимых строк
    :параметр file_path - путь к csv-файлу, подлежащему проверке
    :параметр validation_rules - список регулярных выражений для проверки. Ожидается, что он будет содержать столбец и регулярное выражение
    :возвращает список недопустимых строк
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
        print(f'Error: Произошла ошибка при чтении файла: {e}')
    
    return invalid_rows_list

if __name__ == '__main__':
    invalid_list = validate_csv(FILE_PATH, VALIDATION_RULES)
    
    hash_sum = calculate_checksum(invalid_list)
    serialize_result(variant=35, checksum=hash_sum)