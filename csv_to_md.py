import pandas as pd
from typing import *

def load_data(path):
    df = pd.read_csv(path)
    return df

def remove_unnamed(df):
    new_col_list = df.iloc[0, :].tolist()
    df.columns = new_col_list
    df.reset_index(inplace=True)
    df.drop([0], axis=0, inplace=True)
    df.set_index('index', drop=True, inplace=True)
    df.reset_index(inplace=True, drop=True)
    df.dropna(inplace=True)
    return df

def convert_to_md(df)-> str:
    row, col = len(df.iloc[:, 0]), len(df.iloc[0, :])
    line = ''
    for i in range(row):
        for j in range(col):
            if j == 0:
                line = line + '## intent:' + df.iloc[i][j] + '\n'
            else:
                line = line + df.iloc[i][j] + '\n'
    return line

def write_to_file(filename: str):
    with open(filename, 'w') as output:
        output.write(text)

data = load_data('C:/Users/karma/Downloads/training_unw.csv')
data = remove_unnamed(data)
text = convert_to_md(data)
write_to_file('nlu.md')




# with open('phrases.csv', 'r') as input, open('nlu.txt', 'w') as output:
#     for line in input:
#         line = line.replace(',', '\n')
#         output.write(line)



