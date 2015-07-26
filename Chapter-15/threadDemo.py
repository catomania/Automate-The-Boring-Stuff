#! python3
# threadDemo.py - learning about multithreading
import threading, time
print('Start of the program!')

def takeANap():
	time.sleep(5) #sleep for 5 seconds
	print('Wake up!')

#note: you want to pass the TakeANap() funciton itself as the argument
threadObj = threading.Thread(target=takeANap) #call the TakeANap function in a Thread object, note no parenthesis
threadObj.start() ##chrate the new thread and execute the target function

print('End of program.')

#now why does "end of program" show up before the "Wake up!" part? Hmmm! 
