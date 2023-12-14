import pandas as pd
import json
import re
import logging
from checksum import calculate_checksum, serialize_result

VARIANT = 23

def _read_regexps(path_to_file="regexp_me.json") -> dict:
    '''
    Reading regexp patterns from a file
    '''
    with open(path_to_file, 'r', encoding='utf-8') as fp:
        return json.load(fp)

# Initialize constants by reading from the file
REGEX_PATTERNS = _read_regexps()

def validate_dataframe(df: pd.DataFrame) -> list:
    """Validates rows in a DataFrame

    Args:
        df (pd.DataFrame): DataFrame to validate

    Returns:
        list: List of indices of invalid rows
    """
    invalid_rows = []
    for index, row in df.iterrows():
        # Iterate through each key and validate using the corresponding regex pattern
        if not all(re.match(REGEX_PATTERNS[key], str(row[key])) for key in REGEX_PATTERNS if key in row):
            invalid_rows.append(index)
    return invalid_rows


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    
    dataset = pd.read_csv("23.csv", sep=";", encoding="utf-16")
    
    logger.info("Started validation")
    result = validate_dataframe(dataset)
    logger.info(f"Validation completed")
    
    serialize_result(VARIANT,calculate_checksum(list(result)))
    logger.info("Success")