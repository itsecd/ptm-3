regexps = {
    "telephone": r"^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "height": r"^[12]\.\d{2}$",
    "snils": r"^\d{11}$",
    "identifier": r"^\d{2}-\d{2}/\d{2}$",
    "occupation": r"^[А-Яа-яA-Za-z\s-]+$",
    "longitude": r"^-?(?:(?:/d{0,2}|1[0-8]/d)\.\d+|180\.0+)$",
    "blood_type": r"^(?:A|B|AB|O)[+−]$",
    "issn": r"^\d{4}-\d{4}$",  
    "locale_code": r"^[a-z]{2}(?:\-[a-z]{2})?$",
    "date": r"^\d{4}-(?:0[1-9]|1[0-2])-(?:[0-2]/d|3[01])$"
}