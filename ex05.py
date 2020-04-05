#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#Ex-05 - 3/12/2020

import matplotlib.pyplot as plt
import numpy as np

def getIndex(parts):
    if (parts[0] == ('1' or '2' or '3')):
        if (parts[1] == '1'):
            return 0
        else:
            return 1
    elif (parts[0] == ('4' or '5' or '6')):
        if (parts[1] == '1'):
            return 2
        else:
            return 3
    else:
        if (parts[1] == '1'):
            return 4
        else:
            return 5
        
    
file = open('marketingdata.txt', 'r')
parts = []
counts = [0] * 6

for line in file:
    if 'NA' in line:
        continue
    else:
        parts = line.strip().split()
        index = getIndex(parts)
        counts[index] = counts[index] + 1
        
print('\nLower Income Males:', counts[0], '   Lower Income Females:', counts[1])
print('\nMiddle Income Males:', counts[2], '  Middle Income Females:', counts[3])
print('\nUpper Income Males:', counts[4], '  Upper Income Females:', counts[5])
names = ['Lower Income Males' ,'Lower Income Females' ,'Middle Income Males' ,
         'Middle Income Females' ,'Upper Income Males' ,'Upper Income Females']
yPos = np.arange(len(names))

plt.subplot(1,2,1)
plt.bar(yPos, counts, align = 'center', alpha = 0.5)
plt.xticks(yPos, names, rotation = 'vertical')
plt.ylabel('Income')

plt.subplot(1,2,2)
plt.pie(counts, labels = names, rotatelabels = True)

plt.tight_layout()

plt.show()
