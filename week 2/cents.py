
def getCents(c):
	cents = c
	if(cents == 'done'):
		print("Goodbye.")
		return False
	try:
		cents = int(cents)
	except:
		print("Invalid input. please enter int")
		return True
	if(cents<0):
		print("Invalid input. Please enter postive number")
		return True
	if(cents%5 != 0):
		print("Invalid input. Please enter multiple of five")
		return True
	
	print("You entered",cents , "cents")
	return True

keep_going = True
while(keep_going):
	cents = input("Please enter number that is a muliple of five or done when finished ")
	keep_going = getCents(cents)
	


	


