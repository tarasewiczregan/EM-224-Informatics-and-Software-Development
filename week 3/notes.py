greeting = 'Hello! My name is Regan, it is great meeting you.'
print(greeting.split())

print(greeting.split('!'))

people = open('names.txt', 'r')
print(people)

for raw in people:
    print(raw.split())
    
for raw in people:
    print(raw.strip().split())
    
file = open('names.txt', 'r')

for line in file:
    print(line)

file = open('names.txt', 'r')    
linecount = 0
for linetext in file:
    linecount += 1
    print(linecount, linetext)

file = open('names.txt', 'r')    
count = 0
for line in file:
    count += 1
    print('Line Count:', count)
    
file = open('names.txt')
inp = file.read()
print(len(inp))
print(inp[:20])

fhand = open('names.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('L'):
        continue
    print(line)
    
fhand = open('names.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print(line)
    
myFile = open('myFile.txt', 'w')
myFile.write('This is the first line.\n')
myFile.write('\n')
myFile.write('This is the third line.\n')
myFile.close()

myTuple = ('a', 'b', 'c', 'd')
print(myTuple)
print(myTuple[2])

pop = {'USA' : 320, 'Italy' : 100, 'Japan' : 120}
print(pop['Japan'])
print(pop.keys())
print(pop.values())
print(pop)
pop['UK'] = 64
print(pop)

counts = {'charlie' : 1, 'fred' : 42, 'jan' : 100}
for key in counts:
    print(key, counts[key])
    
print(counts.items())
print(counts.keys())
print(counts.values())

myFile = open('names.txt', 'r')
wordCounter = counter()
for line in myFile:
    words = line.strip().split()
    for word in words:
        try:
            wordCounter += 1
        except:
            wordCounter = 1
first10 = wordCounter.keys()[:10]
for key in first10:
    print(key, wordCounter[key])
