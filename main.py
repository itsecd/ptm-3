import re
import pandas as pd

PATTERNS = {
    "telephone": "\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}",
    "http_status_message": "\d{3} [a-zA-Z0-9_ ]{1,}",
    "snils": "\\d{11}",
    "identifier": "\\d{2}-\\d{2}/\\d{2}",
    "ip_v4": "\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}",
    "longitude": "^-?((180(\\.0+)?|1[0-7]?\\d(\\.\\d+)?|\\d{1,2}(\\.\\d+)?)|0(\\.\\d+)?)$",
    "blood_type": "^(?:O|A|B|AB)[\\+\u2212]$",
    "isbn": "\d+-\d+-\d+-\d+(:?-\d+)?",
    "locale_code": "^([a-z]{2,3})(?:-([a-zA-Z]{2,4}))?(?:-([a-zA-Z0-9-]+))?$",
    "date": "\d{4}-\d{2}-\d{2}"
  }

def check_row(row_str:str) -> bool:
    for key, value in zip(PATTERNS.keys(), row_str):
            print(key, value)
            if key == 'longitude':
                if check_longitude(value) == False:
                    return False
            if key == 'ip_v4':
                if check_ip(value) == False:
                    return False   
            if key == 'snils':
                if check_snils(value) == False:
                    return False  
            if not re.match(PATTERNS[key], value):
                return False
    return True


def check_ip(ip: str) -> bool:
    numbers = list(map(int, re.findall(r'\d{1,3}', ip)))
    for number in numbers:
        if number > 255:
            return False
    return True

def check_snils(snils: str) -> bool:
    if snils[0] == '0':
            return False
    return True


def check_longitude(longitude: str) -> bool:
  
    longitude = float(longitude)
    return -90 < longitude < 90    


def check_item(row_item:str , pattern: str):
    return re.match(pattern, row_item)


def get_invalid_indexs(data:pd.DataFrame) -> list[int]:
    invalid_indexs = []
    
    for index, row in data.iterrows():
        row_str = row
        if not check_row(row):
            invalid_indexs.append(index)
        print(index)
        
       
    return invalid_indexs 

if __name__ == '__main__':
    data = pd.read_csv('2.csv', sep=';', quotechar='"', encoding='utf-16')
    get_invalid_indexs(data)