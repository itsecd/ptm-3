import argparse
import csv
import json
import re
from checksum import calculate_checksum, serialize_result


def read_csv(path_to_csv: str) -> list:
    try:
        with open(path_to_csv, "r", encoding="utf16", newline="") as f:
            reader = csv.DictReader(f, delimiter=';')
            rows_csv = []
            for row in reader:
                rows_csv.append(row)
    except IsADirectoryError as err:
        print(err)            
    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)    
    return rows_csv


def read_json(path_to_json: str) -> dict:
    try:
        with open(path_to_json, "r") as f:
            reader = json.load(f)
    except IsADirectoryError as err:
        print(err)            
    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)          
    return reader


def check_rows(rows_list: list, regexp_dict: dict):
    number_invalid_rows = []
    for key, value in regexp_dict.items():
        for index, row in enumerate(rows_list):
            if not re.match(value, row[key]):
                number_invalid_rows.append(index)
    hash = calculate_checksum(number_invalid_rows) 
    serialize_result(17, hash)           


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-directory_csv', type=str)
    parser.add_argument('-directory_json', type=str)
    try:
        args = parser.parse_args()
        rows_csv = read_csv(args.directory_csv)
        regexp = read_json(args.directory_json)
        check_rows(rows_csv, regexp) 
    except Exception as err:
        print(err)
