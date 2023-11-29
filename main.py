import re
import pandas
from checksum import calculate_checksum, serialize_result

VALIDATION_RULES = {
        "email": r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$',
    "height": r'^\\d\\.\\d{2}$',
    "snils": r'^\\d{11}$',
    "passport": r'^\\d{2}\\s\\d{2}\\s\\d{6}$',
    "occupation": r'^[a-zA-Zа-яА-ЯёЁ\\s-]+$',
    "longitude": r'^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$',
    "hex_color": r'^#([a-f0-9]{6}|[a-f0-9]{3})$',
    "issn": r'^\\d{4}-\\d{4}$',
    "locale_code": r'^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$',
    "time": r'^([01]\\d|2[0-3]):([0-5]\\d):([0-5]\\d)\\.(\\d{1,6})$'
}
FILE_PATH = '35.csv'



def validate_csv(file_path: str, validation_rules: dict[str]) -> list[int]:
    """
    Проверка строк в csv-файле. Эта функция используется для проверки строк csv с помощью регулярного выражения. 
    Она вернет список недопустимых строк
    :параметр file_path - путь к csv-файлу, подлежащему проверке
    :параметр validation_rules - список регулярных выражений для проверки. 
                                Ожидается, что он будет содержать столбец и регулярное выражение
    :возвращает список недопустимых строк
    """
    invalid_rows_list = []
    try:
        df = pandas.read_csv(file_path, sep=';', quotechar='"', encoding='utf-16')
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