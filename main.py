import re
import pandas as pd

from checksum import calculate_checksum, serialize_result


PATTERNS = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": "^\d{3}\s[a-zA-Z0-9_ ]{1,}",
    "inn": "^\d{12}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "ip_v4": "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type": "^(AB|A|B|O)[−+-]?$", 
    "isbn": "^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "uuid": "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$",
    "date": "^\d{4}-\d{2}-\d{2}$",

    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height": "^(?:0|1|2)\.\d{2}$",
    "inn": "^\d{12}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": "^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$",
    "blood_type": "^(AB|A|B|O)[−+-]?$", 
    "issn": "^\d{4}-\d{4}$",
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
        # print(re.match(PATTERNS[value], example)," - ", bool(re.match(PATTERNS[value], example)))
        return False


def get_non_valid_index(df: pd.DataFrame) -> list:
    "via pandas dataframe interate thought row and check each value"
    res = []
    for i in df.index:
    # for i in range(10):
        for j in df.columns.values.tolist():
        # for j in ["isbn","uuid","date"]:
            # print(j, df[j][i], PATTERNS[j])

            if not is_valid(df[j][i], j):
                res.append(i)
                print(df[j][i],re.match(PATTERNS[j], df[j][i]))

                # print(i)
                # print("append is happend")
                break
    return res


if __name__ == "__main__":
    path = "30.csv"
    MY_INDEX = 30
    print(len(get_non_valid_index(get_data(path))))


    
    # serialize_result(MY_INDEX, calculate_checksum(
    #     get_non_valid_index(get_data(path))))
