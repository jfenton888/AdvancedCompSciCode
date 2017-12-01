import sys

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

goingUp = (x < y < z)
goingDown = (z < y < x)

series = (goingUp or goingDown)

print(series)
