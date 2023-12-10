import csv
import re

PATTERNS = {}


def read_csv_file(file_name: str) -> list:
    """
    Reads csv file

    Args: file_name - a string representing the name of the csv file to be read

    Return: a list contains the data from the csv file 

    """
    data = []
    with open(file_name, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for i in reader:
            data.append(i)
        data.pop(0)
    return data


def check_valid_data(data: list) -> bool:
    """
    Check string for data validity.

    Args: A list representing the row of data to be checked.
    
    Return: A boolean value indicating whether the row of data is valid or not.
    
    """
    for key, value in zip(PATTERNS.keys(), data):
        if not re.match(PATTERNS[key], value):
            return False
    return True
