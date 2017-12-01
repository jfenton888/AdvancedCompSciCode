# for i in range(1, 11):
# 	print(i)

# i =52
# while i >= 30:
# 	print(i)
# 	i = i - 2

import sys
timesWrong = 0
Prompts = ["If you want the game to end just get the answer right  ", "Hint: the answer is in the question  "]
correctAnswer = "A Stick"
answer = input("What is brown and sticky?  ")
i = 0
while answer != correctAnswer:
	if timesWrong >= 5:
		i = 1
	timesWrong = timesWrong + 1
	print("That's not the answer I'm looking for, try again  ")
	answer = input(Prompts[i])
