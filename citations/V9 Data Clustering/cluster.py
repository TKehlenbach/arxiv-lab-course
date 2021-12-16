import numpy
from scipy.spatial.distance import cdist
import matplotlib.pyplot as plt
import csv

from tslearn import metrics
from tslearn.clustering import TimeSeriesKMeans
from tslearn.utils import to_time_series_dataset


papers = []
timeSeriesData = []
with open('shortenedTimeSeriesData.csv', mode='r') as dataFile:
    index = 0
    csvFile = csv.reader(dataFile)
    count = 0
    for line in csvFile:
        md = [line[0], line[1]]
        papers.append(md)

        thisPaper = [int(freq) for freq in line[2:]].copy()
        timeSeriesData.append(thisPaper)

X = to_time_series_dataset(timeSeriesData)

print("Data In")
print("Processing...")
km = TimeSeriesKMeans(n_clusters=2, metric="dtw")
labels = km.fit_predict(X)
print("Processed DTW")
print(labels)
# km_bis = TimeSeriesKMeans(n_clusters=2, metric="softdtw")
# labels_bis = km_bis.fit_predict(X)
# print("Processed Soft DTW")
# print(labels_bis)
