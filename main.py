import csv
import re
import checksum


def read_file(filename: str) -> list:
    """
    read file and send every string to check on valid regualr
    filename - name of our variant
    return list_for_checksum - list of indexstring where regular not matched
    """
    first_string = True
    title = ""
    list_for_checksum = []
    index = 0
    with open(filename, "r", encoding="utf-16") as file_it:
        data = csv.reader(file_it, delimiter=";")
        for string in data:
            if first_string:  # catch title string
                first_string = False
                title = string
            else:
                tmp_dict = dict(zip(title, string))  # dict for check string
                if check(tmp_dict):
                    list_for_checksum.append(index)
                index += 1
    return list_for_checksum


def check(string_dict: dict) -> bool:
    """
    string_dict - dict in which key is title and value is current word of string
    return True if value is not matched with regular
    """
    valid = {
        "email": re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
        "http_status_message": re.compile(
            r"(([1-9])|([1-9][0-9])|([1-9][0-9][0-9]))\s[A-Za-z ]"
            ),
        "snils": re.compile(r"^[0-9]{11}$"),
        "passport": re.compile(r"([0-9]{2}\s){2}[0-9]{6}"),
        "ip_v4": re.compile(
            r"^((25[0-5]|2[0-4]\d|1\d\d|\d?\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|\d?\d)$"
        ),
        "longitude": re.compile(r"^-?((1[0-7]\d|\d?\d)(?:\.\d{1,})?|180(\.0{1,})?)$"),
        "hex_color": re.compile(r"\#[0-9a-fA-F]{6}$"),
        "isbn": re.compile(
            r"[0-9]{3}-[0-9]{1}-[0-9]{5}-[0-9]{3}-[0-9]{1}|[0-9]{1}-[0-9]{5}-[0-9]{3}-[0-9]{1}"
        ),
        "locale_code": re.compile(r"[a-z]{2}(-([a-z]){2})?$"),
        "time": re.compile(r"([0-1][0-9]|2[0-3])\:[0-5][\d]\:[0-5][\d]\.[\d]{6}"),
    }

    for title, value in string_dict.items():
        if re.match(valid[title], value) == None:
            return True  # if we found a  not validation value
    return False


if __name__ == "__main__":
    list_of_index_no_valid_strings = read_file("41.csv")
    hash = checksum.calculate_checksum(list_of_index_no_valid_strings)
    checksum.serialize_result(41, hash)