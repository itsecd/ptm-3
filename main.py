import csv
import json
import re
from checksum import serialize_result, calculate_checksum

CSV_PATH = "/Users/vadimkotlarskij/Desktop/Python/ptm-3/29.csv"
REG_JSON_PATH = "/Users/vadimkotlarskij/Desktop/Python/ptm-3/reg.json"


def read_csv(path: str) -> list:
    """ Reads data from a csv file and writes it to a list.

    Arguments:
        path(str): csv file path

    Return value:
        list: a list of data from a csv file
    """
    data = []
    try:
        with open(path, "r", encoding="utf16") as file:
            reader = csv.reader(file, delimiter=";")
            for row in reader:
                data.append(row)
            data.pop(0)
    except Exception as err:
        print(f"Error reading of file:{err}")
    return data


def read_exps(path: str) -> dict:
    """ Reads a json file with regulars and writes it to the dictionary.

    Arguments:
        path(str): path to the controls

    Return value:
        dict: regular expressions read into the dictionary
    """
    data = {}
    try:
        with open(path, "r") as file:
            data = json.load(file)
    except Exception as err:
        print(f"Error reading of file:{err}")
    return data


def chek_row(row: list, exps: dict) -> bool:
    """ Checks whether a data string matches a regular expression.

    Arguments:
        row(list): a string from the dataset
        exps(dict): dictionary of regulars

    Return value:
        bool: True if the string matches the expression. False - otherwise
    """
    for key, value in zip(exps.keys(), row):
        if not re.match(exps[key], value):
            return False
    return True


def validate_data(path_csv: str, path_json: str) -> list:
    """ Records line numbers that do not match regular expressions.

    Arguments:
        path_csv(str): path to dataset
        path_json(str): path to the controls

    Return value:
        list: a list with invalid line numbers
    """
    rows_numbers = []
    data = read_csv(path_csv)
    regexps = read_exps(path_json)
    for i in range(len(data)):
        if not chek_row(data[i], regexps):
            rows_numbers.append(i)
    return rows_numbers


if __name__ == "__main__":
    invalid_rows = validate_data(CSV_PATH, REG_JSON_PATH)
    hash_sum = calculate_checksum(invalid_rows)
    serialize_result(9, hash_sum)