import pytest
import os
import pandas as pd
from project import get_data, get_pdf, table

def test_get_data():
    data = get_data()
    assert isinstance(data, pd.DataFrame)

def test_get_pdf():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    get_pdf(df)
    assert os.path.exists('companies.pdf')

def test_table():
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    table_str = table(df)
    assert isinstance(table_str, str)
