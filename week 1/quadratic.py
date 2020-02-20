#REGAN TARASEWICZ
#"I pledge my honor that I have abided by the Stevens Honor System."
#In-Class Assignment 1, 1/30/2020


#import math

a = float(input("Enter a number a: "))
b = float(input("Enter a number b: "))
c = float(input("Enter a number c: "))

dis = (b**2) - (4*a*c)
ans = ans2 = 0

if (dis == 0):
    ans = 0
    print("Answer: ", ans)
elif (dis > 0):
    ans = (-b - (dis**0.5)) / (2*a)
    ans2 = (-b + (dis**0.5)) / (2*a)
    print("(", ans, ", ", ans2, ")")
else:
    print("Imaginary result.") 
