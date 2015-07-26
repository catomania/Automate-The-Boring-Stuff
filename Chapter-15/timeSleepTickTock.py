#! python3
# timeSleepTickTock.py pauses your program for X seconds and "ticktocks" through the paused time
# need to use SublimeREPL if you are running this on Sublime Text
# my personal Key Binding to run this is ctrl + r

import time

def timerValidation():

	secondsPaused = input("How many seconds would you like to pause for? ")


#user input validation! is it an integer? if so, is it larger than 0 and smaller than 30?
	if secondsPaused.isdigit() == True:

		if int(secondsPaused) > 30:
			print("Don't pause your computer for too long! ")
			timerValidation() #recursion? 

		if int(secondsPaused) <= 0:
			print('Enter an integer larger than zero!')
			timerValidation() #recursion? 

	else:
		if secondsPaused == 'exit': #let the user exit if they want
			print('exiting the program now!')
			exit(0)
		if secondsPaused != 'exit': 
			print('Enter an integer!') #if it's not an exit 
			timerValidation() #recursion? 
		else:
			timerValidation()




	#convert to integer after you have validated your input
	secondsPaused = int(secondsPaused)

#pause the computer for however long the user specified (within reason)
	for i in range(secondsPaused):
		print('Tick')
		time.sleep(0.5) #pause for half a second
		print('Tock')
		time.sleep(0.5)

	print('Done!')
 
	exit(0) #otherwise this function can run FOREVER! Not exactly sure why yet.


#run the program
timerValidation()

