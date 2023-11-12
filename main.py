import re
from pandas import pd
from checksum import calculate_checksum, serialize_result



def validate_input(input_str: str, regex_pattern: str) -> bool:
    """
    Проверяет, соответствует ли входная строка заданному шаблону.
    
    :param input_str: Входная строка для проверки.
    :param regex_pattern: Шаблон для проверки.
    :return: True, если входная строка соответствует шаблону, иначе False.
    """
    regex = re.compile(regex_pattern)
    return bool(re.match(regex, input_str))

def validate_email(email: str) -> bool:
    """
    Validate email format using regular expression
    :param email: str
    :return: bool
    """
    email_regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return validate_input(email, email_regex)

def validate_height(height: Union[str, float]) -> bool:
    """
    Validate height format using regular expression and range check
    :param height: Union[str, float]
    :return: bool
    """
    height_regex = r'^\d+(\.\d+)?$'
    return validate_input(str(height), height_regex) and 1.0 <= float(height) <= 3.0

def validate_snils(snils: str) -> bool:
    """
    Validate SNILS (Russian personal identification number) format using regular expression
    :param snils: str
    :return: bool
    """
    snils_regex = r'^\d{11}$'
    return validate_input(snils, snils_regex)

def validate_passport(passport: str) -> bool:
    """
    Validate passport format using regular expression
    :param passport: str
    :return: bool
    """
    passport_regex = r'^\d{2}\s\d{2}\s\d{6}$'
    return validate_input(passport, passport_regex)

def validate_occupation(occupation: str) -> bool:
    """
    Validate occupation format using regular expression
    :param occupation: str
    :return: bool
    """
    occupation_regex = r'^[А-Яа-я\s]+$'
    return validate_input(occupation, occupation_regex)

def validate_longitude(longitude: Union[str, float]) -> bool:
    """
    Validate longitude format using regular expression
    :param longitude: Union[str, float]
    :return: bool
    """
    longitude_regex = r'^-?\d+(\.\d+)?$'
    return validate_input(str(longitude), longitude_regex)

def validate_hex_color(hex_color: str) -> bool:
    """
    Validate hexadecimal color code format using regular expression
    :param hex_color: str
    :return: bool
    """
    hex_color_regex = r'^#[0-9A-Fa-f]{6}$'
    return validate_input(hex_color, hex_color_regex)

def validate_issn(issn: str) -> bool:
    """
    Validate ISSN (International Standard Serial Number) format using regular expression
    :param issn: str
    :return: bool
    """
    issn_regex = r'^\d{4}-\d{4}$'
    return validate_input(issn, issn_regex)

def validate_locale_code(locale_code: str) -> bool:
    """
    Validate locale code format using regular expression
    :param locale_code: str
    :return: bool
    """
    locale_code_regex = r'^[a-z]{2}-[a-z]{2}$'
    return validate_input(locale_code, locale_code_regex)

def validate_time(time: str) -> bool:
    """
    Validate time format using regular expression
    :param time: str
    :return: bool
    """
    time_regex = r'^\d{2}:\d{2}:\d{2}\.\d{6}$'
    return validate_input(time, time_regex)

if __name__ == '__main__':
    df = pd.read_csv('35.csv', sep=';', quotechar='"', encoding='utf-16')
    invalid_rows = []
    for index, row in df.iterrows():
        is_valid = (
                validate_email(row['email']) and
                validate_height(row['height']) and
                validate_snils(row['snils']) and
                validate_passport(row['passport']) and
                validate_occupation(row['occupation']) and
                validate_longitude(row['longitude']) and
                validate_hex_color(row['hex_color']) and
                validate_issn(row['issn']) and
                validate_locale_code(row['locale_code']) and
                validate_time(row['time'])
        )
        if not is_valid:
            invalid_rows.append(index)
    checksum = calculate_checksum(invalid_rows)
    serialize_result(variant=35, checksumpy=checksum)
    