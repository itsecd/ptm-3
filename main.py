import os
import pandas as pd
import json
import re
from checksum import calculate_checksum, serialize_result

V = 23

def read_regexps(path_to_file ="regexp_me.json") -> json:
    '''
    Считывание regexp'ов 
    '''
    rs = []
    with open(path_to_file, 'r', encoding='utf-8') as fp:
        rs = json.load(fp)
    return rs

def validate_dataframe(df: pd.DataFrame) -> list:
    """Валидация строк

    Args:
        df (pd.DataFrame): DataFrame

    Returns:
        list: Список номеров невалидных строк
    """
    invalid_rows = []
    
    regexps = read_regexps() 

    # Regular expressions for validation

    for index, row in df.iterrows():
        if not (re.match(regexps["email"],row['email']) and
                re.match(regexps["height"],row['height']) and
                re.match(regexps["inn"],row['inn']) and
                re.match(regexps["passport"],row['passport']) and
                re.match(regexps["occupation"],row['occupation']) and
                re.match(regexps["latitude"],row['latitude']) and # Latitude as a decimal number
                re.match(regexps["hex_color"],row['hex_color']) and
                re.match(regexps["issn"],row['issn']) and
                re.match(regexps["uuid"],row['uuid']) and
                re.match(regexps["time"],row['time'])):
            invalid_rows.append(index)

    return invalid_rows

if __name__ == "__main__":
    os.system("cls")
    dataset = pd.read_csv("23.csv", sep=";", encoding="utf-16")
    
    result = validate_dataframe(dataset)
    serialize_result(V,calculate_checksum(list(result)))
    print("success")