import matplotlib.pyplot as plt
import csv

papers = []

with open('finalData_Smooth.csv', mode='r') as dataFile:
    csvFile = csv.reader(dataFile)
    for line in csvFile:
        thisPaper = [float(freq) for freq in line[2:]].copy()
        papers.append(thisPaper)


p1 = 5   #PaperID 52
p2 = 13  #PaperID 86

plt.plot(papers[p1])
plt.plot(papers[p2])
plt.show()
