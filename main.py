import csv
import re
from checksum import serialize_result, calculate_checksum

FILE_PATH = "E:/Study/ptm-3/55.csv"
SAMPLES = {
    "email": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
    "height": "^[1-3]\.\d{2}$",
    "inn": "^\d{12}$",
    "passport": "^\d{2}\s\d{2}\s\d{6}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^-?(?:90(?:\.0+)?|[1-8]?\d(?:\.\d+)?)$",
    "hex_color": "^#([a-f0-9]{6}|[a-f0-9]{3})$",
    "issn": "^\d{4}-\d{4}$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$",
    "time": "^([01]?\d|2[0-3]):([0-5]?\d):([0-5]?\d)\.(\d{1,6})$"
}


def read_file_csv(path: str) -> list[list[str]]:
    '''
    This function for reading data from file csv
    :param path: path to file
    :return: data from file
    '''
    data = []
    with open(path, 'r', encoding="utf-16") as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            data.append(row)
        data.pop(0)
    return data


def check_row_valid(data_row: list[str]) -> bool:
    '''
    This function for checking row validate or not
    :param data: 1 row in table
    :return: True if valid, False if not valid
    '''
    samples = list(SAMPLES.keys())
    for i in range(len(samples)):
        if not bool(re.match(SAMPLES[samples[i]], data_row[i])):
            return False
    return True


def make_list_invalid_number(data: list[list[str]]) -> list[int]:
    '''
    This function for writing the number of invalid rows in list[int]
    :param data: data read from file csv
    :return: List numbers of invalid rows
    '''
    lst = []
    for i in range(len(data)):
        if not check_row_valid(data[i]):
            lst.append(i)
    return lst

if __name__ == "__main__":
    lst_rows = read_file_csv(FILE_PATH)
    invalid_rows = make_list_invalid_number(lst_rows)
    sum = calculate_checksum(invalid_rows)
    serialize_result(55, sum)
