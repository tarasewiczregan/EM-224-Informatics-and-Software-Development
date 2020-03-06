lower = int(input('Enter lower range: '))
upper = int(input('Enter upper range: '))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
            else:
                print(num)
                
                

x = 3
if 2 > x:
    print('First print')
else:
    print('Second')
    if 2 > x:
        print('Third')
    print('Fourth')
print('End')



count = 0
while count < 5:
    print('Hello')
    count += 1
    
print('Goodbye')


mynum = 436
print(mynum/10)


invalue = input('Type an integer number: ')
innum = int(invalue)
if innum % 2 == 0:
    print('EVEN')
else:
    print('ODD')
    