#! python3
#2048_autoplayer.py - play the 2048 game automatically!
#the browser window scrolls when you run this script..

import random

#open browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #so you can send special keys
browser = webdriver.Firefox()

#go to website
browser.get('https://gabrielecirulli.github.io/2048/')

#send keys to game grid
htmlElem = browser.find_element_by_class_name('grid-container')

#scoll all around for 100 times...or until you lose!
for i in range(0, 99):
    direction = random.randint(1, 4) #generates 1 - 4 randomly

    if direction == 1:
        htmlElem.send_keys(Keys.UP) #scroll up
    elif direction == 2:  
        htmlElem.send_keys(Keys.RIGHT) #scroll right
    elif direction == 3:
        htmlElem.send_keys(Keys.DOWN) #scroll down
    else:
        htmlElem.send_keys(Keys.LEFT) #scroll left

