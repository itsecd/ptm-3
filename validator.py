import re

valid_dict = {
    'telephone': re.compile(r'\+7-\([0-9]{3}\)-[0-9]{3}(?:-[0-9]{2}){2}'),
    'height': re.compile(r'[1, 2]\.[0-9]{2}'),
    'inn': re.compile(r'[0-9]{12}'),
    'identifier': re.compile(r'[0-9]{2}-[0-9]{2}\/[0-9]{2}'),
    'occupation': re.compile(r'(?:[а-яА-Яa-zA-Z]+[-|\s]?)+'),
    'latitude': re.compile(r"""(?x)(?:\-?[0-8]\d?\.\d{2,6})| #numbers 0-8.xxxxx, 10-80.xxxxx
                           (?:\-?90\.[0]{6})| #number 90.000000
                           (?:\-?9\.\d{2,6}) #number 9.xxxxxx
                           """),
    'blood_type': re.compile(r"""(?x)(?:[ABO][+|\u2122|−])| #type A, B, O
                             (?:AB[+|\u2122|−] # type AB
                             )""", re.UNICODE),
    'issn': re.compile(r'\d{4}\-\d{4}'),
    'uuid': re.compile(r'[\da-fA-f]{8}(?:-[\da-fA-f]{4}){3}-[\da-fA-f]{12}'),
    'date': re.compile(r"""(?x)(?:18|19|20)\d\d- # year - 18xx, 19xx, 20xx
                       (?:1[0-2]|0[1-9])- #month 1 - 12
                       (?:3[01]|[12]\d|0[1-9]) # day 1 - 31
                       """)
}
    
    
def match_data(research_data :list, names :list) -> tuple:
    """эта функция проверяет данные на корректность

    Args:
        research_data (list): данные для ислледования
        names (list): массив с именами столбцов для доступа к словарю с регулярными выражениями

    Returns:
        tuple(dict, dict): возврощается массив с номерами строк, где были найдены неверные данные
                            и словарь с данными, которые подходят для дальнйшей обработки
    """
    count_not_valid_data = []
    valid_data = {}
    for n in names:
        valid_data[n] = []
    k = 0
    for row in research_data:
        for i in range(10):
            if re.fullmatch(valid_dict[names[i]], row[i]) == None:
                count_not_valid_data.append(k)
            else:
                valid_data[names[i]].append(row[i])
        k += 1
    return rows_not_valid_data, valid_data
            
            