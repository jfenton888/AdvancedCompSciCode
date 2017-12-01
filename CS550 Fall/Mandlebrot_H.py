import tkinter
#import color.sys
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

def FullMand():
	for row in range(HEIGHT):
		for col in range(WIDTH):
			c = complex(xmin + (xmax - xmin) * col / WIDTH, ymin + (ymax - ymin) * row / HEIGHT)
			z = complex(0.0, 0.0)
			# r = mandelbrot(z, c, 0)
			r = mandelbrotloop(z, c)
			#rd = hex(r)[2:].zfill(2)
			rd = hex((r))[2:].zfill(2)
			gr = hex((r*2)%255)[2:].zfill(2)
			bl = hex((r*20)%255)[2:].zfill(2)
			img.put("#" + rd + gr + bl, (col, row))

WIDTH = 640
HEIGHT = 640
xmin = -1.747834073982495
xmax = -1.7478311268188
ymin = 0.006180480701323794
ymax = ymin + xmax-xmin


#size = 0.0009203348559
#xmin = -.105042624716588
#ymin = .6503011843249 #max


maxIt = 255
window = Tk()
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

FullMand()
canvas.pack()
canvas.postscript(file="file_name.ps", colormode='color')
mainloop()