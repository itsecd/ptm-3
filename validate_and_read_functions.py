import csv
import json
import re
from checksum import calculate_checksum, serialize_result

REGEXPS_PATH = "regex_patterns.json"
CSV_PATH = "11.csv"


def read_regex_patterns(path: str) -> dict[str]:
    """function that reads regex patterns from .json file

    Args:
        path (str): path to regex patterns file

    Returns:
        dict: dictionary with regexes
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            regex_patterns = json.load(file)
    except Exception as e:
        print(f"Error while reading .json file: {e}")
    return regex_patterns


def read_csv_file(path: str) -> list[dict[str]]:
    """function that reads data from .csv file

    Args:
        path (str): path to dataset file

    Returns:
        list[dict[str]]: list that contains dictionaries
    """
    dataset = []
    try:
        with open(path, "r", newline="", encoding="utf-16") as file:
            csv_reader = csv.reader(file, delimiter=";")
            for row in csv_reader:
                dataset.append(row)
        dataset.pop(0)
    except Exception as e:
        print(f"Error while reading file with dataset: {e}")
    return dataset


def validate_row(row: list[str], regex_patterns: dict[str]) -> bool:
    """validate a row in a dataset using regular expressions

    Args:
        row (list[str]): a list representing a row in the dataset
        regex_patterns (dict[str]): a dictionary of regular expressions where keys represent
            column names or headers, and values are the corresponding regular expressions
            for validation

    Returns:
        bool: True if the row passes validation based on the provided regular expressions,
            False otherwise.
    """
    for key, value in zip(regex_patterns.keys(), row):
        if not re.match(regex_patterns[key], value):
            return False
    return True


def get_invalid_rows_numbers(csv_path: str, regs_path: str) -> list[int]:
    """
    get the numbers of invalid rows in a CSV file based on provided regex patterns

    Args:
        csv_path (str): the path to the CSV file.
        regs_path (str): the path to the file containing regex patterns in JSON format

    Returns:
        list[int]: a list of row numbers (0-indexed) that are invalid based on the provided
            regex patterns
    """
    invalid_rows_numbers = []
    dataset = read_csv_file(csv_path)
    regs = read_regex_patterns(regs_path)
    for i, row in enumerate(dataset):
        if not validate_row(row, regs):
            invalid_rows_numbers.append(i)
    return invalid_rows_numbers


if __name__ == "__main__":
    invalid_rows_numbers = get_invalid_rows_numbers(CSV_PATH, REGEXPS_PATH)
    hash_sum = calculate_checksum(invalid_rows_numbers)
    serialize_result(11, hash_sum)
