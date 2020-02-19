#REGAN TARASEWICZ
#"I pledge my honor that I have abided by the Stevens Honor System."
#In-Class Assignment 2, 2/06/2020

from datetime import date

name = input('Please enter your name: ')

while True:
    age = input('Please enter your age: ')
    if age == 'done' :
        break
    elif age.isdigit() :
        age = int(age)
        a = int(100 - age)
        year = 2020 + a
        today = date.today()
        future = date(year, 1, 1)
        days = future - today
        print("You will turn 100 in the year: ", year)
        print("That is in ", days.days, " days.")