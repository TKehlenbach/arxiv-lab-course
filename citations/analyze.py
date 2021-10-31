import csv

citationData = []
paperCount = 0

def getData(): 
    global paperCount
    with open('citData.csv', mode ='r')as file:
        csvFile = csv.reader(file)
        
        for line in csvFile:
            if(len(line)>6):
                print(line)
                paperCount += 1

def analyzeData():
    print("Analyzing Data")
    print("Num. Papers :", paperCount)

def main():
    getData()
    analyzeData()

main()