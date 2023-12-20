import pandas as pd
import re
from checksum import calculate_checksum, serialize_result
from regular_expressions import regexps
from typing import List

def find_invalid_rows(data: pd.Series, regexp: str) -> List[int]:

    invalid_rows = list()
    for i in range(len(data)):
        if not re.match(regexp, data[i]):
            invalid_rows.append(i)
    return invalid_rows


if __name__ == "__main__":
    data = pd.read_csv("44.csv", sep = ";", encoding="utf-16")
    invalid_rows = list()
    for key in regexps:
        invalid_rows.extend(find_invalid_rows(data[key], regexps[key]))
    
    checksum = calculate_checksum(invalid_rows)
    serialize_result(44, checksum)
    