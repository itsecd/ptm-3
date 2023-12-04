import re
import pandas as pd

from checksum import calculate_checksum, serialize_result


PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": "^\d{3}\s[a-zA-Z0-9_ ]{1,}$",
    "inn": "^\d{12}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "ip_v4": "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type": "^(AB|A|B|O)[−+-]?$",
    "isbn": "^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "date": "^\d{4}-\d{2}-\d{2}$"
}


def get_data(path: str) -> list:
    "use pandas to read csv"
    return pd.read_csv(path, sep=';', encoding="utf-16")


def is_valid(example, value: str):
    "check example with regular expression via re-module"
    if re.match(PATTERNS[value], example):
        return True
    else:
        return False


def get_non_valid_index(df: pd.DataFrame) -> list:
    "via pandas dataframe interate thought row and check each value"
    res = []
    for i in df.index:
        for j in df.columns.values.tolist():
            if not is_valid(df[j][i], j):
                res.append(i)
                break
    return res


if __name__ == "__main__":
    path = "30.csv"
    MY_INDEX = 30
    serialize_result(MY_INDEX, calculate_checksum(
        get_non_valid_index(get_data(path))))
