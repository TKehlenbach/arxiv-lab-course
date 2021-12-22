import pandas as pd
import numpy as np

name = '../citation-network-dataset/reference_data.feather'
df = pd.read_feather(name)
df = df.replace('nan', np.nan)
cols = ['id', 'year', 'timeline']
timelines = pd.DataFrame(columns=cols)
#stop_at = 10000

for idx, paper in df.iterrows():
    paper_id = paper['_id']
    year = paper['year']

    if paper_id not in timelines['id']:
        temp = pd.Series([paper_id, int(0), list()], index=cols)
        timelines = timelines.append(temp, ignore_index=True)

    timelines.loc[timelines['id'] == paper_id, 'year'] = year

    for r in paper['ref']:
        if r in timelines['id']:
            print('append')
            timelines.loc[timelines['id'] == r, 'timeline'] = timelines.at[timelines['id'] == r, 'timeline'].append(
                year)
        else:
            temp = pd.Series([paper_id, 0, list([year])], index=cols)
            timelines = timelines.append(temp, ignore_index=True)
    print(idx, ' out of ', 5354309, ' (', idx/5354309*100, '%)')
#    if idx == stop_at:
#        break

output = '../citation-network-dataset/timeline_data_small_testset.feather'
timelines = timelines.reset_index()
timelines.to_feather(output)
