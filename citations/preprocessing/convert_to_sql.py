import pandas as pd
import json
import sqlite3
import glob

num_files = len(glob.glob("../citation-network-dataset/split-dataset/" + "*v13.json"))

# Create database
db_name = "../citation-network-dataset/dblp.db"
db = open(db_name, 'w')
db.close()

for file in range(0, num_files):
    # Open JSON data
    filename = "../citation-network-dataset/split-dataset/dblp" + str(file) + ".v13.json"
    f_read = open(filename, 'rb')
    content = f_read.read()
    data = json.loads(content)

    # Create a DataFrame From the JSON Data
    df = pd.DataFrame(data)
    df = df.applymap(str)
    df = df.rename(columns={'references': 'ref'})

    # Write to Database
    conn = sqlite3.connect(db_name)
    table_name = "table" + str(file)
    df.to_sql(table_name, conn)
    print("added table ", file+1, " out of ", num_files)
