def greet(lang):
    if (lang == 'es'):
        print('Hola')
    elif (lang == 'fr'):
        print('Bonjour')
    else:
        print('Hello')
        
greet('en')
greet('es')
greet('fr')


def hello():
    return('Hello')
    
print(hello(), 'Glenn')
print(hello(), 'Sally')


def greet(lang):
    if (lang == 'es'):
        return('Hola')
    elif (lang == 'fr'):
        return('Bonjour')
    else:
        return('Hello')
        
print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')


def addTwo(a, b):
    added = a + b
    return added

x = addTwo(3, 5)
print(x)


def makeSandwich(meat, cheese = 'cheddar', bread = 'rye'):
    print('I will take a sandwich with', meat, cheese, 'and', bread, 'bread')
    
makeSandwich('ham')
makeSandwich('spam', 'cream cheese')


def printAll(*args):        #argument is not a reserved word
    print(*args)
    
printAll(1, 3, 'Hi')


def sqr(x):
    if (x < 0):
        print('There is no root for a negative number.')
        return None
    if (x == 0):
        return 0;
    start = 0
    limit = 100
    for i in range(start, limit, 1):
        if ((i * i) == x):
            return i
        if ((i * i) > x):
            start = i - 1
            limit = i
            
            for j in range (start * 10, limit * 10, 1):
                k = j / 10.0
                if ((k * k ) == x):
                    return k
                if ((k * k) > x):
                    return k
                
print(sqr(15))


def areaTriangle(a, b):
    area = (a / 2.0) * b
    return area

width = 10
height = 15
print('Area of the triangle is:', areaTriangle(width, height))


def foo(x, y):
    global a
    a = 5
    b = 10
    x , y = y , x
    print('Inside foo')
    print('a =', a, '; b =', b, '; x =', x,'; y =', y)
    
a = 1
b = 2
x = 3
y = 4
print('Before foo')
print('a =', a, '; b =', b, '; x =', x,'; y =', y)
foo(25, 30)
print('After foo')
print('a =', a, '; b =', b, '; x =', x,'; y =', y)


def testFunction(n):
    x = n**2
    print(x)
    print(y)
    return None

x = 5
y = 6
print(x)
testFunction(5)
print(x)

import math
x = math.sqrt(16)
print(x)

import math as mth
x = mth.sqrt(16)
print(x)

from math import sqrt
x = sqrt(16)
print(x)

import matplotlib.pyplot as plt

x = range(100)
y = [number ** 2 for number in x]
plt.plot(x,y)
plt.show

x = [1, 2, 3, 4, 5]
y = [12, 24, 0, 9, 15]

plt.subplot(2, 2, 1)
plt.plot(x, y)

plt.subplot(2, 2, 2)
plt.scatter(x, y)

plt.subplot(2, 2, 3)
plt.bar(x, y)

plt.subplot(2, 2, 4)
plt.pie(x)

plt.show


import numpy as np

nlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('Here is the list.')
print(nlist)

mean = sum(nlist) / float(len(nlist))
print('Here is the mean the old way:', mean)

mean2 = np.mean(nlist)
print('Here is the mean the new way:', mean2)
