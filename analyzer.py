import pandas as pd


def read_data(file_path):
    return pd.read_csv(file_path)


def total_sales(df):
    return df["sales"].sum()


def average_sales(df):
    return df["sales"].mean()


def max_sales(df):
    return df["sales"].max()


def min_sales(df):
    return df["sales"].min()


if __name__ == "__main__":
    df = read_data("data.csv")

    print("CSV Data Analyzer")
    print("-----------------")
    print(f"Total Sales: {total_sales(df)}")
    print(f"Average Sales: {average_sales(df)}")
    print(f"Max Sales: {max_sales(df)}")
    print(f"Min Sales: {min_sales(df)}")
