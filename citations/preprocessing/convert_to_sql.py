import numpy as np
import pandas as pd
import json
import sqlite3
import glob

# Create database
db_name = "../citation-network-dataset/dblp.db"
db = open(db_name, 'w')
db.close()

# Connect to database
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Define table
columns = ['_id', 'title', #'venue',
           'year', 'keywords',
           'n_citation', 'lang', #'authors',
           'fos', 'page_start',
           'page_end', 'volume', 'issue', 'issn', 'isbn',
           'doi', 'pdf', 'url', 'abstract', 'ref']

datatypes = ['TEXT', 'TEXT', #'TEXT',
             'INT', 'TEXT[]',
             'INT', 'TEXT', #'TEXT',
             'TEXT', 'TEXT',
             'TEXT', 'TEXT', 'TEXT', 'TEXT', 'TEXT',
             'TEXT', 'TEXT', 'TEXT[]', 'TEXT', 'TEXT[]']

table_name = 'full_data'

create_table = '''CREATE TABLE IF NOT EXISTS ''' + table_name + '''('''

for i in range(len(columns[:-1])):
    create_table += columns[i] + ' ' + datatypes[i] + ','
create_table += columns[-1] + ' ' + datatypes[-1] + ''')'''

c.execute(create_table)
conn.commit()

# Write to table
num_files = len(glob.glob("../citation-network-dataset/split-dataset/" + "*v13.json"))

for file in range(0, num_files):
    # Open JSON data
    filename = "../citation-network-dataset/split-dataset/dblp" + str(file) + ".v13.json"
    f_read = open(filename, 'rb')
    content = f_read.read()
    data = json.loads(content)

    # Create a DataFrame From the JSON Data
    df = pd.DataFrame(data)
    df = df.rename(columns={'references': 'ref'})
    df = df.applymap(str)
    df['year'] = df['year'].astype(float)
    df['year'] = df['year'].replace(np.NaN, -1)
    df['year'] = df['year'].astype(int)
    df['n_citation'] = df['n_citation'].astype(float)
    df['n_citation'] = df['n_citation'].replace(np.NaN, -1)
    df['n_citation'] = df['n_citation'].astype(int)
    df['ref'] = df['ref'].replace(np.NaN, '')
    df = df.drop(['venue', 'authors'], axis=1)
    #print(type(df.loc[1, 'venue']))

    # Write to Database
    number_cols = len(columns) - 1
    insert_command = '''INSERT OR IGNORE INTO ''' + table_name + ''' VALUES (''' + number_cols * '''?,''' + '''?)'''
    for idx, row in df.iterrows():
        c.execute(insert_command, row.to_list())
    conn.commit()
    print("added table ", file+1, " out of ", num_files)

c.close()
conn.close()
