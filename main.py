import os

REG_EXP = {
    "telephone": r"\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}",
    "height": r"\b[0-2]\.\d{1,2}\b",
    "inn": r"\d{12}",
    "identifier": r"\b\d{2}-\d{2}\/\d{2}\b",
    "occupation": r"\B[A-ZА-Я][a-zа-я ^-]+",
    "latitude": r"[-]?\d+\.\d{3,}",
    "blood_type": r"\b(?:AB|A|B|O)[−+-]{1}",
    "issn": r"\b\d{4}\-\d{4}",
    "uuid": r'\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b',
    "date": r"\b\d{4}-(0([13578]-(0[1-9]|[1-2]\d|3[0-1])|[469]-(0[1-9]|[1-2]\d|30)|2-(0[1-9]|1\d|2[0-8])|)|1([02]-"
            r"(0[1-9]|[1-2]\d|3[0-1])|1-(0[1-9]|[1-2]\d|30)))\b"
}


def sum_wrong_lines(file: str) -> int:
    pass


if __name__ == "__main__":
    csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "64.csv")
    print(csv_file)