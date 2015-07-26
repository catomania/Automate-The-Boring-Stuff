#! python3
# countdown.py - plays somme music at the end of 10 seconds


import time, subprocess, winsound

timeLeft = 10
while timeLeft > 0:
	print(timeLeft, end='...')
	time.sleep(1)
	timeLeft = timeLeft - 1

#at the end of the countdown, play your music file!

subprocess.Popen(['start', 'BillieJeanMashUp.wav'], shell=True)
