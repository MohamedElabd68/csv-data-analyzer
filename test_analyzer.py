import pandas as pd
from analyzer import total_sales, average_sales, max_sales, min_sales


def test_total_sales():
    df = pd.DataFrame({"sales": [100, 200, 300]})
    assert total_sales(df) == 600


def test_average_sales():
    df = pd.DataFrame({"sales": [100, 200, 300]})
    assert average_sales(df) == 200


def test_max_sales():
    df = pd.DataFrame({"sales": [100, 200, 300]})
    assert max_sales(df) == 300


def test_min_sales():
    df = pd.DataFrame({"sales": [100, 200, 300]})
    assert min_sales(df) == 100
