#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX-04 - 3/5/2020


def printDetails(data):
    totMiles = totPasses = 0
    for line in data:
        totMiles += float(line[3])
        totPasses += float(line[7])
        
    avgMiles = totMiles / len(data)
    
    print('\nThe following data is from' , data[0][0], 'to' , data[len(data) - 1][0] , ':')
    print('\nThe average miles traveled is' , avgMiles , 'miles.')
    print('The total number of 24-Hour passes purchased is' , totPasses , 'passes.')


fileTxt = open('citi_bike.txt', 'r')
juneTxt = []

for line in fileTxt:
    parts = line.strip().split()
    if parts[0].startswith('6'):
        juneTxt.append(parts)

fileCsv = open('citi_bike.csv', 'r')
januaryCsv = []


for line in fileCsv:
    parts = line.strip().split(',')
    if parts[0].startswith('1'):
        januaryCsv.append(parts)
        
      
printDetails(juneTxt)
printDetails(januaryCsv)

fileTxt.close()
fileCsv.close()

print('\nThis is the end of the files processing.')
