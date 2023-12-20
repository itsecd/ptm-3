import pandas as pd
import re
from checksum import calculate_checksum, serialize_result
from typing import List
import json

REGEXPR = {
    "telephone": "^\\+7-\\(\\d{3}\\)-\\d{3}-\\d{2}-\\d{2}$",
    "height": "^[12]\\.\\d{2}$",
    "snils": "^\\d{11}$",
    "identifier": "^\\d{2}-\\d{2}/\\d{2}$",
    "occupation": "^[А-Яа-яA-Za-z\\s-]+$",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "blood_type": "^(?:A|B|AB|O)[+−]$",
    "issn": "^\\d{4}-\\d{4}$",  
    "locale_code": "^[a-z]{2}(-[a-z]{2})?$",
    "date": "^\\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|1\\d|2[0-9]|3[0-1])$"
}

def find_invalid_rows(data: pd.Series, regexp: str) -> List[int]:

    invalid_rows = list()
    for i in range(len(data)):
        if not re.match(regexp, data[i]):
            invalid_rows.append(i)
    return invalid_rows


if __name__ == "__main__":
    data = pd.read_csv("44.csv", sep = ";", encoding="utf-16")
    invalid_rows = list()
    for key in REGEXPR:
        invalid_rows.extend(find_invalid_rows(data[key], REGEXPR[key]))
    
    checksum = calculate_checksum(invalid_rows)
    serialize_result(44, checksum)
    