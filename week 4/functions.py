#Regan Tarasewicz
#"I pledge my honor that I have abided by the Stevens Honor System.."
#In-class assignment 4 - 2/20/2020

def isNumber(num):
    try:
        int(num)
        return 'yes'
    except:
        return 'no'
    
def factorial(num):
    if num == 0:
        return 1
    else:
        return (num * factorial(num - 1))
    
def calculate(numbers):
    sumNum = 0
    multNum = 1
    for num in numbers:
        sumNum += num
        multNum *= num
    return sumNum, multNum

listNumbers = []

count = 0
while (count < 3):
    print('Input a number..', (count + 1), 'of 3 inputs')
    number = input('->')
    if (isNumber(number) == 'yes'):
        listNumbers.append(int(number))
        count += 1
    else:
        continue
    
print('The factorial of the number', listNumbers[0], 'is', factorial(listNumbers[0]))
sumNumbers, multNumbers = calculate(listNumbers)
print('The numbers added together is equal to', sumNumbers)
print('The numbers multiplied together is equal to', multNumbers)