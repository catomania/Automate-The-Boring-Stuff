#! python3
# drawTextInPython.py - lets you draw some text and save it in a png file!
# please note: the font location is for Windows only
# opportunities to expand this program: specify font size, font, and color!

from PIL import Image, ImageDraw, ImageFont
import os


os.makedirs('myPythonArt', exist_ok=True) #make a folder in your cwd

im = Image.new('RGBA', (500, 500), 'white') #make a white canvas!
draw = ImageDraw.Draw(im)
fontsFolder = 'C:\Windows\Fonts' #this is specific to Windows

def draw_text():
	textDraw = input('What text would you like to draw that is shorter than 50 characters? ')

	if len(textDraw) > 50:
		print('The length of your text is too long! Try again!')
		draw_text()
	else:
		print('Creating your art...')
		arialFont = ImageFont.truetype(os.path.join(fontsFolder, 'arial.ttf'), 32) #get font and size from fontsFolder
		draw.text((200, 200), textDraw, fill='purple', font=arialFont)
		saveFileName = str(textDraw + '.png')
		im.save(os.path.join('myPythonArt', saveFileName))
		print('Done!')
		exit(0)

#is this script being run as the main program or not? 
if __name__ == "__main__":
    draw_text()
