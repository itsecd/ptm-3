import csv
import re

from checksum import calculate_checksum, serialize_result

VARIANT = 6
PATH_TO_CSV = "6.csv"

PATTERNS = {
    "telephone" : r"(\d{3})-(\d{3})-(\d{4})",
    "http_status_message" : "^\\d{3}\\s[^\n\r]+$",
    "inn" : r"(\d{10})",
    "identifier" : r"(\d{15})",
    "ip_v4": "^((25[0-5]|(2[0-4]|1\\d|[1-9]|)\\d)\\.?\\b){4}$",
    "latitude": r"(\d{2}\.\d{6})",
    "blood_type": r"(A|B|AB|0)[+-]",
    "isbn": "\\d+-\\d+-\\d+-\\d+(:?-\\d+)?$",
    "uuid": r"([a-f0-9]{8}-([a-f0-9]{4}-){3}[a-f0-9]{12})",
    "date": r"(\d{2})\.(\d{2})\.(\d{4})",
}
