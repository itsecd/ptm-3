import csv


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
