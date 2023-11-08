import pandas as pd
import re
from checksum import calculate_checksum, serialize_result


def validate_email(email: str) -> bool:
    """
    метод проверки соответствия почты (email) с шаблоном
    re.compile - компилирует регулярное выражение в объект типа шаблон
    re.match - проверяет уже на соответствие шаблону
    :param email: почта
    :return: bool
    """
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    return bool(re.match(pattern, email))


def validate_height(height: str) -> bool:
    """
    метод проверки соответствия роста (height) с шаблоном
    :param height: рост
    :return: bool
    """
    pattern = re.compile(r'^\d+(\.\d{1,2})?$')
    return bool(re.match(pattern, height)) and 1.0 <= float(height) <= 3.0


def validate_snils(snils: str) -> bool:
    """
    метод проверки соответствия снилс с шаблоном
    :param snils: снилс
    :return: bool
    """
    pattern = re.compile(r'^\d{11}$')
    return bool(re.match(pattern, snils))


def validate_passport(passport: str) -> bool:
    """
    метод проверки соответствия паспорта с шаблоном
    :param passport: паспорт
    :return: bool
    """
    pattern = re.compile(r'^\d{2}\s\d{2}\s\d+$')
    return bool(re.match(pattern, passport))


def validate_occupation(occupation: str) -> bool:
    """
    метод проверки соответствия профессия с шаблоном
    :param occupation: профессия
    :return: bool
    """
    pattern = re.compile(r"^[A-Za-zА-Яа-я-'\s]+$")
    return bool(re.match(pattern, occupation))


def validate_longitude(longitude: str) -> bool:
    """
    метод проверки соответствия долготы с шаблоном
    :param longitude: долготы
    :return: bool
    """
    pattern = re.compile(r'^-?\d+(\.\d+)?$')
    return bool(re.match(pattern, longitude))


def validate_hex_color(hex_color: str) -> bool:
    """
    метод проверки соответствия цвета с шаблоном
    :param hex_color: цвет
    :return: bool
    """
    pattern = re.compile(r'^#[0-9A-Fa-f]{6}$')
    return bool(re.match(pattern, hex_color))


def validate_issn(issn: str) -> bool:
    """
    метод проверки соответствия 8-значного международного стандартного
    сериального номера с шаблоном
    :param issn: 8-значный международный стандартный сериальный номер
    :return: bool
    """
    pattern = re.compile(r'^\d{4}-\d{4}$')
    return bool(re.match(pattern, issn))


def validate_locale_code(locale_code: str) -> bool:
    """
    метод проверки соответствия настройки языка с шаблоном
    :param locale_code: региональная настройка языка в формате MS-LCID
    :return: bool
    """
    pattern = re.compile(r'^[a-z]{2}-[a-z]+(,[a-z]{2}-[a-z]+)*$')
    return bool(re.match(pattern, locale_code))


def validate_time(time: str) -> bool:
    """
    метод проверки соответствия времени с шаблоном
    :param time: время
    :return: bool
    """
    pattern = re.compile(r'^([01]\d|2[0-3]):[0-5]\d:[0-5]\d(\.\d{1,6})?$')
    return bool(re.match(pattern, time))

if __name__ == '__main__':
    pass