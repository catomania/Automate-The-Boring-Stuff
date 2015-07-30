#! python3
# resizeAndAddLogo.py - resizes all images in cwd to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner
# note: the cat logo is huge. Not sure how to make the cat logo smaller. Kind of shows up funny.

import os
from PIL import Image #yes, this is case sensitive... 

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'


logoIm = Image.open(LOGO_FILENAME)
logoWidth, logoHeight = logoIm.size #the 'opened logo image' object, not the filename itself

os.makedirs('withLogo', exist_ok=True)

#loop over all files in cwd
for filename in os.listdir('.'):
	if not (filename.endswith('.png') or filename.endswith('.jpg')) \
		or filename == LOGO_FILENAME:
		continue #skip over non-image files and logo file in cwd
	im = Image.open(filename)
	width, height = im.size #get the dimensions of the opened picture file

	#check if image needs to be resized
	if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE: #if both dimensions are larger than 300 pixels
	#calculate new width and height to resize to
		if width > height:
			height = int((SQUARE_FIT_SIZE/width) * height) #resizes height in proportion to width  
			width = SQUARE_FIT_SIZE #set width, the largest dimension, to 300
		else:
			width = int((SQUARE_FIT_SIZE/height) *  width)
			height = SQUARE_FIT_SIZE 

		#resize image
		print("resizing %s..." % (filename))
		im.resize((width, height)) #width and height need to be put in double parenthesis 

	#add logo
	print('Adding logo to %s...' % (filename))
	im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm) #3rd argument is for transparency pixels
	
	#save as new image
	im.save(os.path.join('withLogo', filename)) #saves the new image in the withLogo folder
