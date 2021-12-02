import sqlite3
import pandas as pd
import os
import glob

basepath = os.getcwd()
#num_tables = len(glob.glob(basepath + "/citation-network-dataset/split-dataset/" + "*v13.json"))
num_tables = 54

name = "citation-network-dataset/dblp.db"
conn = sqlite3.connect(name)
df = pd.DataFrame()

# Define your desired columns here
columns = "_id, year, ref"

# Define the name of the output file
output = 'citation-network-dataset/reference_data.feather'

for table in range(0, num_tables):
    command = 'SELECT ' + columns + ' FROM table' + str(table)
    df_app = pd.read_sql(command, conn)
    df = df.append(df_app, ignore_index=True)
    print(table)
df.to_feather(output)