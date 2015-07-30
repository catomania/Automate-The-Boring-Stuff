#! python3
# drawInPython.py - draw different shapes on a blank canvas using the Pillow Image Library!
# needs SublimeREPL to run if using Sublime Text 

from PIL import Image, ImageDraw 
import os

os.makedirs('myPythonArt', exist_ok=True) #make a folder in your cwd


im = Image.new('RGBA', (500, 500), 'white') #create white canvas!

draw = ImageDraw.Draw(im) #sore the ImageDraw object in draw

#ask the user what shape they want to draw

def draw_shape():
	list_shapes = ["line", "rectangle", "ellipse", "polygon"]
	
	print("You can draw any of the following: line, rectangle, ellipse, and polygon. ")

	shape_picked = input('What object would you like to draw? ')

	if shape_picked == "exit":
		print("Now exiting...")
		exit(0)

	elif shape_picked not in list_shapes:
		print ("Error: object not found. Please try again. ")
		draw_shape()

	print("Drawing %s for you now..." % shape_picked)

	
	if shape_picked == "line":
		#draws the shape depending on what was chosen
		draw.line([(0, 0), (199,0)], fill = 'black')
	elif shape_picked == "rectangle":
		draw.rectangle((20, 30, 60, 60), fill='blue')

	elif shape_picked == "ellipse":
		draw.ellipse((120, 30, 160, 60), fill='red')
	else: 
		draw.polygon(((57, 87), (79, 62), (94, 85), (120, 90), (103, 113)), fill='brown')


	#make sure the file is named after the shape
	saveFileName = str(shape_picked + '.png')
	print(saveFileName)

	im.save(os.path.join('myPythonArt', saveFileName))

	print('Done!')

	exit(0)


#is this script being run as the main program or not? 
if __name__ == "__main__":
    draw_shape()
