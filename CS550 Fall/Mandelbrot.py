

xs = float(input('position start'))
xf = float(input('position final'))
step = float(input('step by'))
xc = xs
yc = xs
def mandi(xc , yc):
	counter += 1
	if (xc**2) + (yc**2) >= 4:
		return counter
	else:
		xl = x
		yl = y
		counter += 1
		mandi(xl**2 yl**2 + xo, 2*xo*yo)

while (yc > yf) and (xc > xf):	
	if (xc > xf):
		yc += 1
		xc = 0
	xo = xs
	yo = xs
	x = xo
	y = yo
	xl = xc
	yl = yc
	counter = 0
	print(mandi())
	xc += 1
	
