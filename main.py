import csv
import re
from checksum import serialize_result, calculate_checksum

PATTERN = {
    "telephone": "^\+7-\(\d{3}\)-\d{3}-\d{2}-\d{2}$",
    "http_status_message": "^\d{3}\s[a-zA-Z0-9_ ]{1,}$",
    "shils": "^\d{11}$",
    "identifier": "^\d{2}-\d{2}/\d{2}$",
    "ip_v4": "^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",
    "longitude": "^-? \d{1,3} \. \d+$",
    "blood_type": "^(?: AB | A | B | O) [+\u2212]$",
    "isbn": "^\d+-\d+-\d+-\d+(:?-\d+)?$",
    "locale_code": "^[a-z]{2} (-[a-z]{2})?$",
    "date": "^\d{4}-\d{2}-\d{2}$"
}