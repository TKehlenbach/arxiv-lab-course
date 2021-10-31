import csv

citationData = []
papersDates = dict()
paperIndices = dict()


def getDatesAndIndices():
    global papersDates, paperIndices, citationData
    with open('hep-th-slacdates', 'r') as fd:
        count = 0
        for row in fd:
            line = row.replace("\n", '').replace(",", '').replace("'", '').strip()
            
            if not line: #Handle empty lines
                continue 

            paperID, paperDate = line.split(' ')

            # Add "paperID : paperDate" to dictionary
            papersDates[paperID] = paperDate

            # Add [paperID] to citationData
            citationData.append([paperID])

            # Add "paperID : count" to paperIndices
            paperIndices[paperID] = count

            if count<10:
                print(paperID, paperDate, count)

            count += 1

def buildRevCitation():
    global citationData
    with open('hep-th-citations', 'r') as fc:
        count = 0
        for row in fc:
            line = row.replace("\n", '').replace(",", '').replace("'", '').strip()
            
            if not line: #Handle empty lines
                continue

            citer, citee = line.split(' ')

            if(citer in paperIndices): #If the citing paper has a date
                if(citee in paperIndices):
                    citationData[paperIndices[citee]].append(papersDates[citer]) 

            if count<10:
                print(citer,citee)
            count += 1

def writeCitationDataToFile():
    global citationData
    with open('citData.csv', 'w', newline='') as f: 
        write = csv.writer(f) 
        write.writerows(citationData) 


def main():
    getDatesAndIndices()
    print("")
    buildRevCitation()
    writeCitationDataToFile()


main()


