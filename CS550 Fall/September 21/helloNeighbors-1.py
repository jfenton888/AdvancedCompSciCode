#  end='' keeps the cursor in the same line that it was writting in in that print operator
#  otherwise it would move the cursor to the next line after ever individual calling for a print

# To run the code you would input python3 helloNeighbors.py and then three names


import sys

names = ["John", "Henry", "Palmer", sys.argv[1], sys.argv[2], sys.argv[3]]

for x in range(0, 3):
	print("Hello, "+ names[x] + "!")

for x in range(3, 6):
	if names[x] in ["Mrs. Healy", "Healy", "Hoke" "Meghan", "Ms. Hoke", "Mrs Healy"]:
		print(names[x] , ", thank you for joining us!")
	else: 
		print(names[x] , ", what are you doing here? This isn't your table!")
