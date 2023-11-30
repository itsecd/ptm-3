import re
import csv
import checksum 

 
PATTERNS = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", # Done
    "height": "^(?:0|1|2)\.\d{2}$",  # Done
    "snils": "^\d{11}$", #Done
    "passport": "^\d{2} \d{2} \d{6}$", # Done 
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$", # Done
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$", # Done ?
    "hex_color": "^#[0-9a-fA-F]{6}$", # Done
    "issn": "^\d{4}-\d{4}$", # Done ?
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "time": "^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$" # Done
  }

def read_csv(name="3"):
    '''
        Считывание csv файла

        name(str): имя csv файла
        returns: данные с  файла без первой строки
    '''
    data = []
    with open(f"{name}.csv", "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    data.pop(0)
    return data

def check_invalid_row(row: list) -> bool:
    '''
        Функция проверки каждой строки на валидность
    '''
    for patterns, item in zip(PATTERNS.keys(), row):
        if not re.search(PATTERNS[patterns], item):
            return False
    return True


def get_no_invalid_data_index(data: list) -> list:
    '''
        Функция находит невалидные строки и записывает их индексы 
    '''
    index_list = []
    index = 0
    for row in data:
        if not check_invalid_row(row):
            index_list.append(index)
        index += 1
    return index_list


if __name__ == "__main__":
    data= read_csv()
    invalid_data = get_no_invalid_data_index(data)
    hash = checksum.calculate_checksum(invalid_data)

    checksum.serialize_result(3, hash)