import csv
import re
import checksum


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
            first_it = True
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                dict_of_data[keys[col]].append(row[col])
            dict_of_data[keys[col]].pop(0)
            print(len(dict_of_data[keys[col]]))
    return dict_of_data


def check(dict_data: dict) -> bool:
    """Передаем прочитанные данные, возвращаем список из индексов невалидных значений"""


if __name__ == "__main__":
    dict_data = read_file("20.csv")
    list_no_valid_value = check(dict_data)
