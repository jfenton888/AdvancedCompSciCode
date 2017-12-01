import tkinter
from tkinter import *

def mandelbrot(z, c, count):
	z = z * z + c
	count += 1
	if abs(z) >= 2.0 or count > maxIt-1:
		return count
	return mandelbrot(z, c, count)

def mandelbrotloop(z, c):
	count = 0
	while abs(z) < 2.0 and count < maxIt-1:
		z = z * z + c
		count += 1
	return count


WIDTH = 640
HEIGHT = 640
maxIt = 255


#First Picture

#verY very small window
#focused in on a part of what would be the zipper of the mandlebrot set
xmin1 = -.105042624716588
xmax1 = -0.1041222899
ymin1 = 0.6493808495
ymax1 = .6503011843249


window1 = tkinter.Toplevel()
canvas1 = Canvas(window1, width = WIDTH, height = HEIGHT, bg = "#000000")
img1 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas1.create_image((0, 0), image = img1, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex(xmin1 + (xmax1 - xmin1) * col / WIDTH, ymin1 + (ymax1 - ymin1) * row / HEIGHT)
        z = complex(0.0, 0.0)
        r = mandelbrotloop(z, c)
        #regular mandlebrot code
        rd = hex((r*2)%255)[2:].zfill(2)
        gr = hex((r*2)%255)[2:].zfill(2)
        bl = hex((r*20)%255)[2:].zfill(2)
        img1.put("#" + rd + gr + bl, (col, row))
#sets color for set, off white i sthe center color, not black, and it moves out to blue with a yellow transition
canvas1.pack()

canvas1.postscript(file="file_name.ps", colormode='color')



#Second Picture

#focuses in to a less common pattern of the set by going far in
xmin2 = -1.1201118973452442
xmax2 = -1.120006127986316
ymin2 = .27639108055963235
ymax2 = ymin2 + xmax2-xmin2


window2 = tkinter.Toplevel()
canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")
img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex(xmin2 + (xmax2 - xmin2) * col / WIDTH, ymin2 + (ymax2 - ymin2) * row / HEIGHT)
        z = complex(0.0, 0.0)
        r = mandelbrotloop(z, c)
        #regular mandlebrot code
        rd = hex((r*2)%255)[2:].zfill(2)
        gr = hex((r*2)%255)[2:].zfill(2)
        bl = hex((r*20)%255)[2:].zfill(2)
        img2.put("#" + rd + gr + bl, (col, row))
#same colors as the first set, becuase they looked so col
canvas2.pack()
canvas2.postscript(file="file_name.ps", colormode='color')







#Third Picture

#focuses in ver close to a section of the set that's somewhat unique becuase of its position far to the negative x and close to y=0
xmin3 = -1.747834073982495
xmax3 = -1.7478311268188
ymin3 = 0.006180480701323794
ymax3 = ymin3 + xmax3-xmin3


window3 = tkinter.Toplevel()
canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")
img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)

for row in range(HEIGHT):
    for col in range(WIDTH):
        c = complex(xmin3 + (xmax3 - xmin3) * col / WIDTH, ymin3 + (ymax3 - ymin3) * row / HEIGHT)
        z = complex(0.0, 0.0)
        r = mandelbrotloop(z, c)
        #regular mandlebrot code
        rd = hex((r))[2:].zfill(2)
        gr = hex((r*2)%255)[2:].zfill(2)
        bl = hex((r*20)%255)[2:].zfill(2)
        img3.put("#" + rd + gr + bl, (col, row))
#different color set tht uses a more green and red color theme 

canvas3.pack()
canvas3.postscript(file="file_name.ps", colormode='color')


mainloop()


