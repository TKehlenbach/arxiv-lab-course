import sqlite3
import pandas as pd
import numpy as np


def convert_string_col_to_list(text):
    if type(text) == str:
        text = text.replace('[', '')
        text = text.replace(']', '')
        text = text.replace('\'', '')
        text = text.split(', ')
        return text
    else:
        return list()


name = '../citation-network-dataset/dblp.db'
output = '../citation-network-dataset/reference_data.feather'
conn = sqlite3.connect(name)
c = conn.cursor()

# Define your desired columns here
columns = '_id, year, ref'

# Define the name of the new table
table = 'full_data'
select_command = 'SELECT ' + columns + ' FROM ' + str(table)
df = pd.read_sql(select_command, conn)
df = df.replace('nan', np.nan)
df['ref'] = df['ref'].apply(convert_string_col_to_list)
df.to_feather(output)
conn.close()
