import csv
import json

def read_csv(path_to_csv: str) -> list:
    try:
        with open(path_to_csv, "r", encoding="utf16", newline="") as f:
            reader = csv.DictReader(f, delimiter=';')
            rows_csv = []
            for row in reader:
                rows_csv.append(row)
    except IsADirectoryError as err:
        print(err)            
    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)    
    return rows_csv

def read_json(path_to_json: str) -> dict:
    try:
        with open(path_to_json, "r") as f:
            reader = json.load(f)
    except IsADirectoryError as err:
        print(err)            
    except FileNotFoundError as err:
        print(err)
    except Exception as err:
        print(err)          
    return reader
