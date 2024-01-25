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


def f(column_name, xin):
    df = data_loader()
    da = df[column_name].values
    d = (da.max() - da.min()) / xin

    xi = []
    for i in range(xin):
        xi.append("[%d, %d)" % (da.min() + d * i, da.min() + d * (i + 1)))
    return # column_values_counted


# for test
if __name__ == '__main__':
    df = data_loader('Top_scientists_2022.csv')
    # print(len(df.index))
    bins = np.linspace(0, 1, 50, endpoint=False)
    print(bins)
    indices = np.digitize(df['sm-field-frac'], bins)
    print(indices)
    a = pd.Series(indices).value_counts()#.sort_index().tolist()
    print(a)

