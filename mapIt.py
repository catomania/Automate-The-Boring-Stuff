#! python3
#mapIt.py - launches a map in the browser using the address from the
#command line or clipboard
#makes launching Google Maps less tedious!

import webbrowser, sys, pyperclip #sys is for reading command line arguments

#is there a command line argument? 
if len(sys.argv) > 1: #has a command line argument been provided?
    #get address from command line.
    address = ' '.join(sys.argv[1:])#command line arguments are usually separated by spaces.
    #why 1:? Because you want to chop off the first element of the array and store the rest as address
else:
    #get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address) 
