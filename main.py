import csv

PATTERNS = {
    "telephone": r'\+7 - \(\d{3}\) - \d{3} - \d{2} - \d{2}',
    "height": "^(?:0|1|2)\.\d{2}$",
    'inn': r'\d{12}',
    'identifier': r'\d{2} - \d{2} / \d{2}',
    "occupation": "^[a-zA-Zа-яА-ЯёЁ\s-]+$",
    "latitude": r'-? \d+ \. \d+',
    "blood_type": r'(?: AB | A | B | O) [+−]',
    "issn": "^\d{4}\-\d{4}$",
    "uuid": r'[0-9a-f]{8} - [0-9a-f]{4} - [0-9a-f]{4} - [0-9a-f]{4} - [0-9a-f]{12}',
    "date": r'\d{4} - \d{2} - \d{2}',
}


def get_data(filename: str):
    """
    Получение данных из csv файла.
    :param filename: Имя файла.
    """
    data = []
    with open(filename, "r", newline="", encoding="utf-16") as file:
        read_data = csv.reader(file, delimiter=";")
        for row in read_data:
            data.append(row)
    return data


if __name__ == '__main__':
    data = get_data("56.csv")