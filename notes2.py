#REGAN TARASEWICZ
#"I pledge my honor that I have abided by the Stevens Honor System."
#In-Class Assignment 2, 2/06/2020

x = 10
type(x)

y = 1.3
type(y)

print(x + y)
print(x * y)
print(x * 3)

name = 'Regan '
last = 'Tarasewicz'
type(name)
print(name + last)
print(name * 4)             #prints name four times


height = 'five feet'
if type(height) == str:
    print("I am " + height + " tall")
elif type(height) == int:
    print('My height is: ', height)
else:
    print('There is no data.')
    
x = 10
y = float(x)
z = int(y)
w = str(z)
print('My number is: ' , w * 2)

type(w)

age = 'fifteen'
new_age = int(age)          #cannot convert strings to int, unless it is a digit

var_1 = input('What is the first variable? ')
if var_1.isdigit() == False:
    print(var_1, ', is not a number')
else:
    print(var_1, ', is a number')
    
var_2 = input('What is the second variable?')
try:
    num = float(var_2)
    print(num, ', is a number')
except:
    print(var_2, ', is not a number')
    
name = input('What is your name?')
print('Hello ' + name)

inp = input("Europe floor? ")
usf = int(inp) + 1
print("US floor: ", usf)

ex_list = [1, 2, 'abc', 'fish']
print(ex_list[0])
print(ex_list[3])

ex_list[3] = 'tilapia'
print(ex_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8]
print(mylist[3])
print(mylist[3:])
print(mylist[:3])
print(mylist[-3:])
print(mylist[-1])

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b           #concatenation
print(c)

a = [1, 2, 3]
b = [4, 5, 6]
a.append(b)
print(a)

a = [234, 133, 42]
42 in a
55 in a
55 not in a

classes = ['math', 'chemistry', 'history', 'gym']
schedule = ['P1', 'P2', 'P3', 'P4']

for i in [0, 1, 2, 3] :
    print(schedule[i], classes[i])

a = [457, 246, 110, 111]
a.sort()
print(a)

b = ['spam', 'eggs', 'bacon']
b.sort()

mystring = 'Good Morning America!'
print(mystring[5])
print(mystring[5:])

for letter in mystring:
    print(letter)

print(mystring.lower())
print(mystring.upper())
print(mystring.title())
print(mystring.capitalize())
print(mystring.startswith('Go'))
print(mystring.startswith('Am'))

classes = ['math', 'chemistry', 'history', 'gym']
word = 'dog'

social = '777-55-6879'

print(list(social))

last4 = social[-4:]
for c in social:
    if c.isdigit():
        social = social.replace(c, 'x')
        
print(social[:-4] + last4)

newlist = [1, 2, [3, 4], 5]
print(newlist[2][1])
print(newlist.index(5))

while True:
    line = input('> ')
    if line == 'done' :
        break
    print(line)

print('Done!')

while True :
    line = input('> ')
    if line[0] == '#' :
        continue