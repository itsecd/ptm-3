import json

PATTERNS = {
    'telephone': r'\+7 - \(\d{3}\) - \d{3} - \d{2} - \d{2}',
    'http_status_message': r'\d{3} \s .+',
    'inn': r'\d{12}',
    'identifier': r'\d{2} - \d{2} / \d{2}',
    'ip_v4':  r'\d{1,3} \. \d{1,3} \. \d{1,3} \. \d{1,3}',
    'latitude': r'-? \d+ \. \d+',
    'blood_type': r'(?: AB | A | B | O) [+−]',
    'isbn': r'\d+ - \d+ - \d+ - \d+ (?: -\d+)?',
    'uuid': r'[0-9a-f]{8} - [0-9a-f]{4} - [0-9a-f]{4} - [0-9a-f]{4} - [0-9a-f]{12}',
    'date': r'\d{4} - \d{2} - \d{2}',
}

if __name__ == '__main__':
    with open('patterns.json', 'w') as fp:
        json.dump(PATTERNS, fp)
