import argparse
import csv
import json
import logging
import re
from checksum import calculate_checksum, serialize_result

logger = logging.getLogger()
logger.setLevel('INFO')


def read_csv(path_to_csv: str) -> list:
    """Reads the file, creates a list of lines read from csv.
    Args:
        path_to_csv (str): Psth to file.
    Returns:
        list: List of lines read from csv.
    """
    try:
        with open(path_to_csv, "r", encoding="utf16", newline="") as f:
            reader = csv.DictReader(f, delimiter=';')
            rows_csv = []
            for row in reader:
                rows_csv.append(row)
    except IsADirectoryError as err:
        logging.error(f"Error with the csv {err}")          
    except FileNotFoundError as err:
        logging.error(f"Error with the csv {err}")     
    except Exception as err:
        logging.error(f"Error with the csv {err}")     
    return rows_csv


def read_json(path_to_json: str) -> dict:
    """Reads and writes regular expressions to the dictionary.
    Args:
        path_to_json (str): Psth to file.
    Returns:
        dict: Regular expressions for each column from csv.
    """
    try:
        with open(path_to_json, "r") as f:
            reader = json.load(f)
    except IsADirectoryError as err:
        logging.error(f"Error with the json {err}")           
    except FileNotFoundError as err:
        logging.error(f"Error with the json {err}") 
    except Exception as err:
        logging.error(f"Error with the json {err}")         
    return reader


def check_rows(rows_list: list, regexp_dict: dict):
    """Checks all csv strings for compliance with a regular expression, 
    calls hash calculation functions from line numbers and writes the result to json.
    Args:
        rows_list (list): lines from csv.
        regexp_dict (dict): regular expressions to check.
    """
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
        logging.error(f"Error {err}")  
