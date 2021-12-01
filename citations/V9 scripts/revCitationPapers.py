import csv

paperDates = dict()
revCitationList = []
revCitationListIndices = dict()


with open('paperDates.csv', mode='r')as paperDatesFile:
    index = 0
    csvFile = csv.reader(paperDatesFile)
    for line in csvFile:
        paperIndex = line[0]
        paperPublishDate = line[1]
        paperDates[paperIndex] = paperPublishDate

        revCitationList.append([paperIndex, paperPublishDate])
        revCitationListIndices[paperIndex] = index
        index += 1

# print(paperDates)

with open('citData.csv', mode='r')as citationDataFile:
    csvFile = csv.reader(citationDataFile)
    count = 0
    for line in csvFile:
        # print('###', line[0], '###')
        for citesPaper in line[2:]:
            # print(citesPaper, paperDates[int(citesPaper)])
            # print(revCitationList[revCitationListIndices[int(citesPaper)]])
            try:
                index = revCitationListIndices[citesPaper]
                revCitationList[index].append(line[0])
            except KeyError: 
                print("No paper with index :", citesPaper)
            # print(revCitationList[index])
        # count += 1
        # if(count > 13):
        #     break

with open('revCitationPapers.csv', 'w', newline='') as f: 
        write = csv.writer(f) 
        write.writerows(revCitationList) 
