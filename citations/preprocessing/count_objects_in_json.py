import pandas as pd
import json
import sqlite3
import os
import glob

num_tables = 54
columns = ['_id', 'title', 'venue', 'year', 'keywords', 'n_citation', 'lang',
       'authors', 'fos', 'page_start', 'page_end', 'volume', 'issue', 'issn',
       'isbn', 'doi', 'pdf', 'url', 'abstract', 'ref']

name = "../citations/citation-network-dataset/dblp.db"
conn = sqlite3.connect(name)
c = conn.cursor()
create_table = '''CREATE TABLE IF NOT EXISTS citations('''
for col in columns[:-1]:
    create_table += col + ''' TEXT,'''
create_table += columns[-1] + ''' TEXT)'''

c.execute(create_table)
c.execute('''CREATE UNIQUE INDEX IF NOT EXISTS citations_id ON citations(_id)''')
c.execute('''SELECT * FROM citations''')
conn.commit()

for table in range(0, num_tables):
    select_command = 'SELECT * FROM table' + str(table)
    c.execute(select_command)
    data = c.fetchall()
    insert_command = '''INSERT OR IGNORE INTO citations VALUES (''' + 19*'''?,''' + '''?)'''
    for row in data:
        c.execute(insert_command, row[1:])
    conn.commit()
    print('Inserted table ', table)
    delete_command = '''DROP TABLE table''' + str(table)
    c.execute(delete_command)
    print('Deleted table', table)

c.close()
conn.close()
