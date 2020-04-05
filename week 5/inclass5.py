#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System."
#In-class Assignment 5, Due 2/27/2020

import re

def validate(temp):
    for i in temp:
        if (len(i) < 6) or (len(i) > 12):
            continue
        
        if not re.search('[a-z]', i):
            continue
        
        if not re.search('[0-9]', i):
            continue
        
        if not re.search('[A-Z]', i):
            continue
        
        if not re.search('[$#@]', i):
            continue
    
        finalPass.append(i)
        
        
passw = input("Please enter possible passwords, separated by commas: ")
passwords = passw.split(',')
finalPass = []
validate(passwords)
    
print('The following are the acceptable passwords:')
print(*finalPass, sep = ', ')
if len(finalPass) == 0:
    print('No passwords worked.')
