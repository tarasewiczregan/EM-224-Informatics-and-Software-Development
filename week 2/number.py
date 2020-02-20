#REGAN TARASEWICZ
#"I pledge my honor that I have abided by the Stevens Honor System."
#In-Class Assignment 2, 2/06/2020
          

while True:
    line = input('Please enter a number: ')
    if line == 'done' :
        break
    elif line.isdigit() :
        num = int(line)
        if num == 4 :
            print('You entered 4!')
        elif (num % 2) == 0 :
            print(num, ' is an even number.')
        else :
            print(num, ' is an odd number.')
        
print('Done')    

    