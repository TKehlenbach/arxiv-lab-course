import pandas as pd
import numpy as np

name = "../citation-network-dataset/reference_data.feather"
df = pd.read_feather(name)
df = df.replace('nan', np.nan)
cols = ['id', 'year', 'timeline']
timelines = pd.DataFrame(columns=cols)

for idx, paper in df.iterrows():
    paper_id = paper['_id']
    year = paper['year']

    if paper_id not in timelines['id']:
        temp = pd.DataFrame([[paper_id, 0, list()]], columns=cols)
        timelines = timelines.append(temp)

    timelines.loc[timelines['id'] == paper_id, 'year'] = year

    refs = paper['ref']

    if type(refs) == str:
        refs = refs.replace('[', '')
        refs = refs.replace(']', '')
        refs = refs.split(',')

        for r in refs:

            if r in timelines['id']:
                timelines.loc[timelines['id'] == r, 'timeline'] = timelines.at[timelines['id'] == r, 'timeline'].append(
                    year)
            else:
                temp = pd.DataFrame([[paper_id, 0, list([year])]], columns=cols)
                timelines = timelines.append(temp)
    print(idx)
output = '../citation-network-dataset/timeline_data.feather'
timelines.to_feather(output)
