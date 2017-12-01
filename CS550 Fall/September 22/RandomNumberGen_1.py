import random

play = 1
while play == 1:
	numGen = int(random.uniform(1,100))
	numPick = int(input("Pick a number between 1 and 100"))
	print(numGen)
	while numGen != numPick:
		if numGen == numPick:
			print("Correct")
		else if numPick < numGen:
			print("Too Low")
		else if numPick > numGen:
			print("Too High")
	play = int(input("Want to play again? 1 or 0"))
