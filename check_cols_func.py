import re


def check_data_col(input_date: str) -> bool:
    date = list(map(int, re.findall(r'\d+', input_date)))
    return 0 < date[0] < 2025 and 0 < date[1] < 13 and 0 < date[2] < 32


def check_ipv4(input_ip: str) -> bool:
    numbers = list(map(int, re.findall(r'\d{1,3}', input_ip)))
    for number in numbers:
        if number > 255:
            return False
    return True


def check_longitude(input_longitude: str) -> bool:
    return float(input_longitude) > -180.0 and float(input_longitude) < 180.0
