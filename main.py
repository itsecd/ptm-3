import csv
import re
import checksum
import logging

def read_file(filename: str) -> dict:
    """
    Читаем файл, записываем каждый столбец в словарь, где ключ это заголовок, значения это массив значений
    """
    dict_of_data = {'telephone': [],
                    "height": [],
                    "snils": [],
                    "identifier": [],
                    "occupation": [],
                    "longitude": [],
                    "blood_type": [],
                    "issn": [],
                    "locale_code": [],
                    "date": []
                    }
    keys = list(dict_of_data.keys())
    for col in range(10):
        with open(filename, "r", encoding="utf-16") as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                dict_of_data[keys[col]].append(row[col])
            dict_of_data[keys[col]].pop(0)
            logger.debug("%d values are read in the column %s", len(dict_of_data[keys[col]]), keys[col])
    return dict_of_data


def check(dict_data: dict) -> list:
    """Передаем прочитанные данные, возвращаем список из индексов невалидных значений"""
    valid = {
        'telephone': re.compile(r"\+7\-\(\d\d\d\)\-\d\d\d\-\d\d\-\d\d"),
        "height": re.compile(r"[1-2]\.[0-9]{2}$"),
        "snils": re.compile(r"^[0-9]{11}$"),
        "identifier": re.compile(r"[0-9]{2}\-[0-9]{2}\/[0-9]{2}$"),
        "occupation": re.compile(r"^[a-zA-Zа-яА-ЯёЁ\s-]+$"),
        "longitude": re.compile(r"^-?((1[0-7]\d|\d?\d)(?:\.\d{1,})?|180(\.0{1,})?)$"),
        "blood_type": re.compile(r"^(?:AB|A|B|O)(?:[\−|\+])$"),
        "issn": re.compile(r"^[0-9]{4}\-[0-9]{4}$"),
        "locale_code": re.compile(r"^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$"),
        "date": re.compile(r"^[0-9]{4}\-[0-9]{2}\-[0-9]{2}")
    }

    list_no_valid_value = []
    for key in dict_data.keys():
        for i in range(len(dict_data[key])):
            if re.match(valid[key], dict_data[key][i]) is None:
                list_no_valid_value.append(i)
    return list_no_valid_value


if __name__ == "__main__":
    logger = logging.getLogger("df")
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s')
    logger.setLevel(logging.DEBUG)
    dict_data = read_file("20.csv")
    list_no_valid_val = check(dict_data)
    my_hash = checksum.calculate_checksum(list_no_valid_val)
    checksum.serialize_result(20, my_hash)
