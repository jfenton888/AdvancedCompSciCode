import sys

names = ["John", "Henry", "Palmer", sys.argv[1], sys.argv[2], sys.argv[3]]
response =[]

for x in range(0, 3):
	response = input ("Hello, "+ names[x] + "!" + "What is your favorite food?")

