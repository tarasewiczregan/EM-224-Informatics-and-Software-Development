#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#Ex-03 - 2/20/2020

while True:
    fileName = input("Please enter file name, with no extension: ")
    if fileName == 'marketingdata':
        fileName = fileName + '.txt'
        break
    else:
        print('Incorrect file name.')
        continue
    
file = open(fileName, 'r')

lineCount = 0
naCount = 0

print('\nThese are the three first lines with NA')
for line in file:
    if 'NA' in line:
        if naCount < 3:
            print(line)
        naCount += 1
    lineCount += 1
    
print('\nThe file has', lineCount, 'lines, of which', naCount, 'have NA in them.')

file = open('CitiBike.csv', 'r')

firstFive = []
lessMiles = []
lineCount = 0

next(file)

for line in file:
    line = line.strip().split(',')
    
    if lineCount < 5:
        firstFive.append(line)
    lineCount += 1
    
    try:
        miles = int(line[3])
    except:
        continue
    
    if miles < 10000:
        lessMiles.append(line)
        
print('\nThese are the first five lines of the file: ')
for lines in firstFive:
    print(lines)
    
print('\nThese are the lines with "Miles Traveled Today" smaller than 10,000: ')
for lines in lessMiles:
    print(lines)
    
print('\nThe file has', lineCount, 'lines.')