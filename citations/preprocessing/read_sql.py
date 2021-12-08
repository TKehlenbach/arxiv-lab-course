import sqlite3
import pandas as pd


def convert_string_to_list(text):
    text = text.replace('[', '')
    text = text.replace(']', '')
    text = text.replace('\'', '')
    text = text.split(',')
    return text


name = "../citation-network-dataset/dblp.db"
conn = sqlite3.connect(name)
c = conn.cursor()

# Define your desired columns here
columns = "_id, year, ref"

# Define the name of the new table
table = 'complete_data'
select_command = 'SELECT ' + columns + ' FROM ' + str(table)
c.execute(select_command)
data = c.fetchall()

datatypes = ['TEXT', 'INT', 'TEXT[]']

for row in data:
    print(row)
    row_listed = list(row)
    for i in range(len(row_listed)):
        print(i, row_listed[i])
        if i in (3, 5, 11, 12):
            if row_listed[i] in nulltypes:
                row_listed[i] = row_listed[i].replace(row_listed[i], '-1')
            row_listed[i] = int(float(row_listed[i]))
        elif i in (4, 8, 17, 19):
            row_listed[i] = convert_string_to_list(row[i])
        print(row_listed[i])

    row = tuple(row_listed)



c.close()
conn.close()


df = pd.read_sql(command, conn)
df.to_feather(output)
