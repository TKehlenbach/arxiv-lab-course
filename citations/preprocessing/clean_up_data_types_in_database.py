import pandas as pd
import json
import sqlite3
import os
import glob

name = "../citation-network-dataset/dblp.db"
conn = sqlite3.connect(name)
c = conn.cursor()
select_command = 'ALTER TABLE citations RENAME TO complete_data'
c.execute(select_command)
c.close()
conn.close()