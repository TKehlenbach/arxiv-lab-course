import sqlite3
import pandas as pd


def convert_string_to_list(text):
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('\'', '')
    text = text.split(',')
    return text


name = "../citation-network-dataset/dblp.db"
output = "../citation-network-dataset/reference_data.feather"
conn = sqlite3.connect(name)
c = conn.cursor()

# Define your desired columns here
columns = "_id, year, ref"

# Define the name of the new table
table = 'full_data'
select_command = 'SELECT ' + columns + ' FROM ' + str(table)
df = pd.read_sql(select_command, conn)
print(df)
#df.to_feather(output)
conn.close()
