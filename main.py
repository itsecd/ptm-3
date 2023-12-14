import os
import pandas as pd
import re
from checksum import calculate_checksum, serialize_result

V = 23

def validate_dataframe(df):
    invalid_rows = []

    # Regular expressions for validation
    email_regex = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    height_regex = re.compile(r'^(?:0|1|2)\.\d{2}$')
    inn_regex = re.compile(r'^\d{12}$')
    passport_regex = re.compile(r'^\d{2} \d{2} \d{6}$')
    occupation_regex = re.compile(r'^[a-zA-Zа-яА-ЯёЁ\s-]+$')
    lattitude_regex = re.compile(r'^(-?[1-8]?\d(?:\.\d{1,})?|90(?:\.0{1,})?)$')
    hex_color_regex = re.compile(r'^#[0-9a-fA-F]{6}$')
    issn_regex = re.compile(r'^\d{4}-\d{4}$')
    uuid_regex = re.compile(r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$')
    time_regex = re.compile(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)\.(\d{1,6})$')

    for index, row in df.iterrows():
        if not (email_regex.match(row['email']) and
                height_regex.match(str(row['height'])) and
                inn_regex.match(str(row['inn'])) and
                passport_regex.match(row['passport']) and
                occupation_regex.match(row['occupation']) and
                lattitude_regex.match(str(row['latitude'])) and # Latitude as a decimal number
                hex_color_regex.match(row['hex_color']) and
                issn_regex.match(row['issn']) and
                uuid_regex.match(row['uuid']) and
                time_regex.match(row['time'])):
            invalid_rows.append(index)

    return invalid_rows

if __name__ == "__main__":
    os.system("cls")
    dataset = pd.read_csv("23.csv", sep=";", encoding="utf-16")
    
    result = validate_dataframe(dataset)
    serialize_result(V,calculate_checksum(list(result)))
    print("success")