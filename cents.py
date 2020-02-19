#REGAN TARASEWICZ
#"I pledge my honor that I have abided by the Stevens Honor System."
#EX-03, 2/13/2020

while True:
    cents = input("Enter a number of cents, as a multiple of five, or type done.\n")
    
    if (cents == "done") : 
        print("All done!")
        break
    
    try : 
        cents = int(cents)
    except :
        print("Invalid input, try again with numericals.\n")
        continue
    
    if (cents % 5 != 0) :
        print("Invalid input, try again with multiple of 5.\n") 
        continue
    
    if (cents <= 0) :
        print("Invalid input, try again with number greater than zero.\n")
        continue
    
    print("You inputed ", cents, " cents.")
    
    