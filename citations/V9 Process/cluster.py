import numpy
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import csv

from tslearn import metrics
from tslearn.clustering import TimeSeriesKMeans
from tslearn.utils import to_time_series_dataset


papers = []
timeSeriesData = []
with open('finalData_Smooth.csv', mode='r') as dataFile:
    index = 0
    csvFile = csv.reader(dataFile)
    count = 0
    for line in csvFile:
        md = [line[0], line[1]]
        papers.append(md)

        thisPaper = [float(freq) for freq in line[2:]].copy()
        timeSeriesData.append(thisPaper)

        count += 1
        if count>1000:
            break

X = to_time_series_dataset(timeSeriesData)

print("Data In")
print("Processing...")
km = TimeSeriesKMeans(n_clusters=8, metric="dtw")
labels = km.fit_predict(X)
print("Processed 1")
# km_bis = TimeSeriesKMeans(n_clusters=2, metric="softdtw")
# labels_bis = km_bis.fit_predict(X)
# print("Processed 2")
# print(labels[:100])

output = [[papers[i][0], papers[i][1], labels[i]] for i in range(0, len(papers))]

with open('clusteringOutput.csv', 'w', newline='') as f: 
        write = csv.writer(f) 
        write.writerows(output) 


