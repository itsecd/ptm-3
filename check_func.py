import re
def check_ip(ip: str) -> bool:
    """
    Функция, которая проверяет диапазон чисел в ip_v4

    :param ip: айпишник, который нужно проверить
    :return: возвращет True, если айпишник прошел валидацию, False - иначе
    """
    ip_numbers = list(map(int, re.findall(r'\d{1,3}', ip)))   
    for ip_number in ip_numbers:
        if ip_number > 255:
            return False
    return True


def check_date(date: str) -> bool:
    """
    Функция, которая проверяет дату

    :param date: дата, которую нужно проверить
    :return: возвращет True, если дата прошела валидацию, False - иначе
    """
    date = list(map(int, re.findall(r'\d+', date)))
    return 0 < date[0] < 2125 and 0 < date[1] < 13 and 0 < date[2] < 32


def check_longitude(longitude: str) -> bool: 
    """
    Функция, которая проверяет широту

    :param longitude: широта, которую нужно проверить
    :return: возвращет True, если широта прошела валидацию, False - иначе
    """   
    longitude = float(longitude)
    return -180 < longitude < 180 