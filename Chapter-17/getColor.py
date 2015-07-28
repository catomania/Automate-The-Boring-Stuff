#! python3
# getColor.py - sends back RGBA values depending on what color you pick using Pillow
# I use CTRL-R as a keybinding in Sublime Text to run this

def returnColor():

	from PIL import ImageColor
	try:
		while True:
			print('What color would you like RGBA values for?')
			colorDesired = input("Color: ")
			print(str(ImageColor.getcolor(colorDesired, 'RGBA')))

	except ValueError:
		print('Color does not exist! Try again!')
		returnColor()

#is this script being run as the main program or not? 
if __name__ == "__main__":
    returnColor()
