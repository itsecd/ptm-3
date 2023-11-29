import re
import pandas as pd

def get_data(path: str) -> list:
    return pd.read_csv(path)