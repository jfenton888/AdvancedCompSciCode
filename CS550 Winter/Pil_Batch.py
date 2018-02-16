from PIL import Image, ImageFilter, ImageChops
import numpy as np
import sys

camein = sys.argv[1]
theysaid = camein.split(",") #splits up each name in the input to seperate files that can be edited seperately
for i in range(len(theysaid)): #runs the program again for each image name inputted
	pixels = np.asarray(Image.open(theysaid[i]))
	#pixels.setflags(write = 1)
	#pixels[: , : , 1:2] = 0

	pixels = Image.fromarray(np.uint8(((pixels+25)*-1)*2)) #filters  the colors, the *-1 creates the most interesting change
	pixels = Image.fromarray(np.fliplr(pixels)) #mirrors the image over left right 
	pixels = pixels.filter(ImageFilter.SMOOTH) #smooths the colors, internal to numpy

	pixels.rotate(180).show() #rotates the image, made it full 180 so it looks fine
	theysaid[i] = (theysaid[i])[0:(len(theysaid[i])-4)] #strips the file type off the previous file name
	pixels.save(theysaid[i] + '_1' + '.jpg') # saves the image, adding _1 to the end of the file name and makes it a jpg

#on my honor I have neither given nor recieved unauthorized aid
#Jack Fenton