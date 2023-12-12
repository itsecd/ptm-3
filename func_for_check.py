import re


def check_ip(ip: str) -> bool:
    """
    Функция, которая проверяет диапазон чисел в ip_v4

    :param ip: ip, который нужно проверить
    :return: возвращет True, если ip прошел валидацию, False - иначе
    """
    ip_numbers = list(map(int, re.findall(r'\d{1,3}', ip)))
    for ip_number in ip_numbers:
        if ip_number > 255:
            return False
    return True


def check_time(time: str) -> bool:
    """
    Функция, которая проверяет время

    :param time: время, которое нужно проверить
    :return: возвращет True, если time прошело валидацию, False - иначе
    """
    time = list(map(int, re.findall(r'\d+', time)))
    return 0 < time[0] < 24 and 0 < time[1] < 60 and 0 < time[2] < 60
