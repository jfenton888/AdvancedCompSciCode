import sys

names = ["John", "Henry", "Palmer", sys.argv[1]]


for x in range(0, 3):
	currentName = names[x]
	print("Hello, "+ currentName + "!")
#if names[3] == "Mrs. Healy" or names[3] == "Healy" or names[3] == "Meghan" or names[3] == "Ms. Hoke" or names[3] == "Mrs Healy":
print(names[3].find("Healy"))

if names[3] in ["Mrs. Healy", "Healy", "Meghan", "Ms. Hoke", "Mrs Healy"]:
	print(names[3] + ", thank you for joining us!")
else: 
	print(names[3] , " what are you doing here? This isn't your table!")
