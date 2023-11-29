import csv
import re
from typing import List
from checksum import calculate_checksum, serialize_result


REGEX_PATTERNS: dict[str, str] = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": r"^\d{3}\s[a-zA-Z0-9_ ]{1,}",
    "inn": r"^\d{12}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "ip_v4": r"^(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
             r"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
             r"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\."
             r"(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
    "latitude": r"^(-?[1-8]?\d(?:\.\d+)?|90(?:\.0+)?)$",
    "blood_type": r"^(AB|A|B|O)[−+-]?$",
    "isbn": r"^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "uuid": r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "date": r"^\d{4}-\d{2}-\d{2}$"
}

VARIANT: int = 41
CSV_FILE_PATH: str = "41.csv"
CSV_ENCODING: str = "utf-16le"


def is_row_valid(row: List[str]) -> bool:
    """
    Determine if a row from the CSV file is valid.

    A row is considered valid if all its fields match the corresponding regex patterns defined in REGEX_PATTERNS.

    :param row: A list of strings, where each string is a field in the CSV row.

    :return bool: True if the row is valid, False otherwise.
    """
    return all(re.search(REGEX_PATTERNS[field], value) for field, value in zip(REGEX_PATTERNS, row))


def get_invalid_row_indices(data: List[List[str]]) -> List[int]:
    """
    Identify all invalid rows within the dataset based on the regex patterns.

    :param data: The dataset read from the CSV file, where each inner list represents a row.

    :return List: A list of indices that correspond to the invalid rows in the dataset.
    """
    return [index for index, row in enumerate(data) if not is_row_valid(row)]


def main() -> None:
    """
    This function opens the CSV file, reads its contents excluding the header, validates each row with the defined
    regex patterns, calculates the checksum of invalid row indices, and then serializes the checksum result using the
    serialize_result function.
    """
    with open(CSV_FILE_PATH, "r", newline="", encoding=CSV_ENCODING) as file:
        reader = csv.reader(file, delimiter=";")
        data: List[List[str]] = list(reader)[1:]

    invalid_indices: List[int] = get_invalid_row_indices(data)
    checksum_value: str = calculate_checksum(invalid_indices)

    serialize_result(VARIANT, checksum_value)


if __name__ == "__main__":
    main()