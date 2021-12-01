
#*A polynomial time generator for minimal perfect hash functions
#@Thomas J. Sager
#t1985
#cCommunications of the ACM
#index1492
#%31957
#%319567
#%320477
#%2135000

import csv

data = []
dataCount = 0
newDataPoint = False
thisDataPoint = []
yearPublished = 2000
paperIndex = 0
count=0
with open('acm.txt', 'r') as fread, open('citData.csv', 'w', newline='') as fwrite:
    write = csv.writer(fwrite)
    for row in fread:
        line = row.replace("\n", '').strip()
        if(line.startswith('#t')):
            data.append(thisDataPoint)
            # print(thisDataPoint)
            write.writerow(thisDataPoint)
            count += 1
            print("Rows Written :",count)
            thisDataPoint = []
            yearPublished = line[2:]
        
        if(line.startswith('#index')):
            paperIndex = line[6:]
            thisDataPoint.append(paperIndex)
            thisDataPoint.append(yearPublished)

        if(line.startswith('#%')):
            refIndex = line[2:]
            thisDataPoint.append(refIndex)

# with open('citData.csv', 'w', newline='') as f: 
#         write = csv.writer(f) 
#         write.writerows(data) 