'''
Regan Tarasewicz
"I pledge my honor that I have abided by the Stevens Honor System."
Exam 1, Section 3
'''

'''
This section takes an input and first checks if the length is equal to 1.
If length is 1, it searches the character for the vowels, 
either lower or upper case
'''
import re

print('Part one.\n')
char = input('Enter a character and I will check if it is a vowel: ')
if len(char) != 1:
    print('False.')
else:
    if re.search('[aeiou]', char):
        print('True')
    elif re.search('[AEIOU]', char):
        print('True')
    else:
        print('False')
        
'''
This section first opens and reads the file word_list.csv into a dictionary
Then it checks the length of the words and saves whichever is longest of each comparison
Also saves length to a total counter to calculate average
'''
print('\nPart two.')
file = open('word_list.csv', 'r')
length = 0
maximum = 0
longest = 'a'

words = dict()
for line in file:
    parts = line.strip().split(',')
    for i in parts:
        if i in words:
            words[i] = words[i] + 1
        else:
            words[i] = 1
            


for key in list(words.keys()):
    if len(key) > maximum:
        maximum = len(key)
        longest = key
        
    length += len(key)
    
print('\nAverage length:' , length/len(words))
print('Longest word:', longest)


'''
This section inputs a word and for each character in that word
it repeats the character the same amount of times as the length
of the original word, saves it to a new string and prints that
'''
print('\nPart three\n.')
word = input('Enter a word: ')
new = ''
for character in word:
    new = new + (character)*len(word)
    
print(word , '--->' , new)