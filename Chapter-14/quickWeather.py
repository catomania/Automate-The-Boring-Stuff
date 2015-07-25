#! python3
# quickWeather.py - prints the weather from command line
# or clipboard

import json, requests, sys, pyperclip

#compute location from command line arguments
#or...from the clipboard!

if len(sys.argv) < 2:
	location = pyperclip.paste() #or set to San Francisco for testing
else: location = ' '.join(sys.argv[1:])

#DL the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3' % (location)
response = requests.get(url)
response.raise_for_status() #check for errors

#Load JSON data into a Python variable
weatherData = json.loads(response.text)

#print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'])
print("\n")
print("Tomorrow's weather:")
print(w[1]['weather'])
