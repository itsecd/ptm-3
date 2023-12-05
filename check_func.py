import re


def check_ip(ip: str) -> bool:
    """
    A function that checks the range of numbers in ip_v4
    :param ip: IP address to be checked
    ::return: returns True if the IP address has passed validation, False - otherwise
    """
    ip_numbers = list(map(int, re.findall(r"\d{1,3}", ip)))
    for ip_number in ip_numbers:
        if ip_number > 255:
            return False
    return True


def check_date(date: str) -> bool:
    """
    A function that checks the date
    :param date: the date to be checked
    ::return: returns True if the date has passed validation, False - otherwise
    """
    date = list(map(int, re.findall(r"\d+", date)))
    return 0 < date[0] < 2125 and 0 < date[1] < 13 and 0 < date[2] < 32


def check_longitude(longitude: str) -> bool:
    """
    A function that checks the longitude
    :param longitude: the longitude to be checked
    ::return: returns True if the longitude has passed validation, False - otherwise
    """
    longitude = float(longitude)
    return -180 < longitude < 180