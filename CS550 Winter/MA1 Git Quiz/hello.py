import sys

names = ["John", "Henry", "Palmer", 0]


for x in range(0, 3):
	currentName = names[x]
	print("Hello, "+ currentName + "!")
	if x == 2:
		names[3]= input('And what is your name? ')