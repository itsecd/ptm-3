import csv
import json
import re
from checksum import calculate_checksum, serialize_result

JSON_PATH = "regexps.json"
CSV_PATH = "25.csv"


def read_csv(file_path: str) -> list:
    """Reads data from a csv file and returns a list of rows as nested lists.

    Args:
        file_path: The path to the csv file.

    Returns:
        A list of lists, each containing the values of a row in the csv file.

    Raises:
        Exception: If there is an error while reading the file.
    """
    data = []
    try:
        with open(file_path, "r", encoding="utf16") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)
            for row in reader:
                data.append(row)
    except Exception as e:
        print(f"Error while reading {file_path}: {e}")
    return data


def read_json(path_json: str) -> dict:
    """Reads a JSON file with regular expressions and writes them to a dictionary.

    Args:
        path_json: The path to the file to be read.

    Returns:
        A dictionary where the keys are the names of the regular expressions and the values are the regular expressions themselves.

    Raises:
        Exception: If there is an error while reading the file.
    """
    try:
        with open(path_json, "r") as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error while reading {path_json}: {e}")
        return {}


def verify_row(row: list, expressions: dict) -> bool:
    """Check if a row of data matches a regular expression.

    Args:
        row (list): A row from a dataset.
        expressions (dict): A dictionary of regular expressions.

    Returns:
        bool: True if the row matches the expression, False otherwise.
    """
    for key, value in zip(expressions.keys(), row):
        if not re.match(expressions[key], value):
            return False
    return True


def verify_data(path_csv: str, path_json: str) -> list:
    """Returns a list of row numbers that do not match the regular expressions.

    Args:
        path_csv (str): The path to the dataset file.
        path_json (str): The path to the file with regular expressions.

    Returns:
        list: A list of invalid row numbers.
    """
    invalid_rows = []
    data = read_csv(path_csv)
    regexps = read_json(path_json)
    for i, row in enumerate(data):
        if not verify_row(row, regexps):
            invalid_rows.append(i)
    return invalid_rows


if __name__ == "__main__":
    invalid_rows = verify_data(CSV_PATH, JSON_PATH)
    hash_sum = calculate_checksum(invalid_rows)
    serialize_result(25, hash_sum)
