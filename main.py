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
