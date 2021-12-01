import csv

# paperDates = dict()
paperDatesList = []
count = 0

with open('citData.csv', mode='r')as file:
    csvFile = csv.reader(file)
    for line in csvFile:
        # paperDates[paperIndex] = paperDate
        # paperDates[int(line[0])] = int(line[1])
        paperDatesList.append([line[0], line[1]])

# print(paperDates)

with open('paperDates.csv', 'w', newline='') as f: 
        write = csv.writer(f) 
        write.writerows(paperDatesList) 

