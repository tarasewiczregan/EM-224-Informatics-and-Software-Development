#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#In class assignment 3 - 2/13/2020

file = open('names.txt', 'r')
name = dict()

for line in file:
    line = line.strip().split()
    for word in line:
        if word in name:
            name[word] += 1
        else:
            name[word] = 1
        
for key in list(name.keys()):
    print(key, name[key])
print(len(name))
    
file = open('names.txt', 'a')
file.write('\nMost common name:')
file.write(max(name, key=name.get))
file.close()
