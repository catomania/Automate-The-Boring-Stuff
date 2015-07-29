#! python3
# zophiePaster.py covers the original zophie image with tons of cat heads! Just for fun!

from PIL import Image
from random import randint

catIm = Image.open('zophie.png')
catCopyIm = catIm.copy() #make a copy of the Zophie the cat

#crop Zophie's face
faceIm = catIm.crop((355, 354, 565, 560))

for i in range(100):
	#catCopyIm.paste(faceIm, (randint(0, 606), (randint(0,873))) #upper limits are Zophie picture minus face crop dimensions
	#catCopyIm.paste(faceIm, (100, 200))
	catCopyIm.paste(faceIm, (randint(0, 606), randint(0, 873))) #careful with the parens!

#save the new cat photos
catCopyIm.save('cat_pasted.png')
