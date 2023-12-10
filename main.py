import csv

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

