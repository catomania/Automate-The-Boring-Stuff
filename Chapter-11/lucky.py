#! python3
#lucky.py - opens several Google search results.
#you will need the Beautiful Soup module

import requests, sys, webbrowser, pyperclip, bs4 #bs4 is Beautiful Soup!

print('Googling...') #display text while dling Google page


#check for argument
if len(sys.argv) > 1:
    getURL = ' '.join(sys.argv[1:])
else:
#if no argument, use clipboard text
    getURL = pyperclip.paste()
    
#go to the desired google search results page
res = requests.get('http://google.com/search?q=' + getURL)

#check the status
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

#Retrieve top search results
soup = bs4.BeautifulSoup(res.text) 

#Open browser tab for each result
linkElems = soup.select('.r a') #r class and a element
numOpen = min(5, len(linkElems)) #open up 5 tabs or less 
for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href')) 

