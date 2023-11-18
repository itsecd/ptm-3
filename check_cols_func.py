import re


def check_data_col(input_date: str) -> bool:
    '''
    Проверка даты на валидность (чтобы не было 13 месяца в году и тд.)
    :params input_date: input date needed to validate
    '''
    date = list(map(int, re.findall(r'\d+', input_date)))
    return 0 < date[0] < 2125 and 0 < date[1] < 13 and 0 < date[2] < 32


def check_ipv4(input_ip: str) -> bool:
    '''
    Проверка ip_v4 на валидность
    :params input_ip: input ip_v4 needed to validate
    '''
    numbers = list(map(int, re.findall(r'\d{1,3}', input_ip)))
    for number in numbers:
        if number > 255:
            return False
    return True


def check_longitude(input_longitude): return abs(
    float(input_longitude)) < 180.0
