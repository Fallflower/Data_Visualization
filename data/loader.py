import pandas as pd
# from illustrations import *
import numpy as np


def data_loader(file_name="./data/Top_scientists_2022.csv"):
    df = pd.read_csv(file_name, encoding='ISO-8859-1')
    return df


def count_by_column(column_name):
    df = data_loader()
    column_values_counted = df[column_name].value_counts(ascending=False)
    return column_values_counted


if __name__ == '__main__':
    df = data_loader('Top_scientists_2022.csv')
    a = df['inst_name'].value_counts(ascending=False)
    print(a)
