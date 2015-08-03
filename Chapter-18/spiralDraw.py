#! python3
# spiralDraw.py - make a fun spiral!
# note: I keep on getting a WinError5 message when I try to run this..weird! It looks like I can't actually write any 
# code that contains pyautogui.dragRel without getting an error message
import pyautogui, time

time.sleep(5) #gives you time to move your mouse
pyautogui.click() #click to put drawing program into focus
distance = 200 #this number gets smaller as you go through your loop

while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2) #move right and pause
	distance = distance - 5
	pyautogui.dragRel(0, distance, duration=0.2) #move down 
	distance = distance - 5
	pyautogui.dragRel(-distance, 0, duration=0.2) #move left
	distance = distance - 5
	pyautogui.dragRel(0, -distance, duration=0.2) #move up

