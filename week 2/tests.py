file = open('names.txt', 'r')

for line in file:
    print(line)
    
linecount = 0
for linetext in file:
    linecount += 1
    print(linecount, linetext)
    