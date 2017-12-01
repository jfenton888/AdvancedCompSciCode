import sys

t = float (sys.argv[1])
v = float (sys.argv[2])
w = float (0)

if abs(t) <= 50 and 3<= v and v <= 120:
	w = 35.74 + 0.6215*t + (0.4275*t - 35.75)*v*0.16
	print(w , end='')
	print("˚ F")
else:
	print("Wave off RubberDucky, wave off! We have a problem!")
