import pandas as pd
import numpy as np

name = "../citation-network-dataset/reference_data.feather"
df = pd.read_feather(name)
df = df.replace('nan', np.nan)
timelines = {}
stopper = 0
for idx, paper in df.iterrows():
    paper_id = paper['_id']
    year = paper['year']
    if paper_id not in timelines.keys():
        timelines[paper_id] = {}
    timelines[paper_id]['year'] = year
    if 'timeline' not in timelines[paper_id].keys():
        timelines[paper_id]['timeline'] = []
    refs = paper['ref']
    print(refs)
    if type(refs) == str:
        refs = refs.replace('[', '')
        refs = refs.replace(']', '')
        refs = refs.split(',')
        for r in refs:
            print(r)
            if r in timelines.keys():
                timelines[r]['timeline'].append[year]
            else:
                timelines[paper_id] = {}
                timelines[paper_id]['timeline'] = [year]
    stopper += 1
    if stopper == 10:
        break
print(pd.DataFrame.from_dict(timelines, orient='index'))
print(df[['_id', 'year', 'ref']].head(10))
