import sqlite3
import pandas as pd

name = "../citation-network-dataset/dblp.db"
conn = sqlite3.connect(name)

# Define your desired columns here
columns = "_id, year, ref"

# Define the name of the output file
output = '../citation-network-dataset/reference_data.feather'
table = 'citations'
command = 'SELECT ' + columns + ' FROM ' + str(table)
df = pd.read_sql(command, conn)
df.to_feather(output)
