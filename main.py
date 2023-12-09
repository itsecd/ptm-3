import csv
import json
import re

JSON_PATH = "regexps.json"


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
        with open(file_path, "r") as csv_file:
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
    for i, exp in expressions.items():
        if not re.match(exp, row[i]):
            return False
    return True


def verify_data(path_csv: str, path_json: str) -> list:
    """
    Checks if the rows of a dataset match the regular expressions
    Arguments:
        path_csv (str): the path to the dataset
        path_json (str): the path to the regular expressions
    Return value:
        list: a list of invalid row numbers
    """
    invalid_rows = []
    with open(path_json, "r") as f:
        regex_dict = json.load(f)
    with open(path_csv, "r") as f:
        for i, row in enumerate(f):
            values = row.strip().split(",")
            valid = True
            for value, regex in zip(values, regex_dict.values()):
                pattern = re.compile(regex)
                match = pattern.match(value)
                if not match:
                    valid = False
                    break
            if not valid:
                invalid_rows.append(i + 1)
    return invalid_rows
