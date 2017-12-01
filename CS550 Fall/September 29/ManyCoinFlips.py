import random
import math
flipResult = []

bigNum = int(input("How many times would you like to flip the coin?"))
if bigNum >= 1000000:
	sizeofList = bigNum
else:
	sizeofList = 1000000	

for i in range(0 , sizeofList):
	
	curResult = random.randint(0 , 1)
	# print(curResult)
	flipResult.append(curResult*100)
total = sum(flipResult[:bigNum])
avg = total//bigNum
# for i in range(bigNum):
# 	print(flipResult[i])
print("percent of heads after ", str(bigNum), "coin flips ", end="")
print(avg)

for e in range(1 , 6):
	PofTen = 10**e
	total = sum(flipResult[:PofTen])
	avg = total//PofTen
	print("percent of heads after ", str(PofTen), "coin flips is " , str(avg))



import random 

def coinFlip()
	result = random.randint(0 , 1)
	



# import random
# import math
# flipResult = []

# bigNum = int(input("How many times would you like to flip the coin?"))

# for i in range(0 , bigNum):
	
# 	curResult = random.randint(0,1)
# 	print(curResult)
# 	flipResult.append([curResult])



# total = sum(flipResult)
# avg = total//bigNum
# print("percent of heads after ", str(bigNum), "coing flips", end="")
# print(avg)

# for e in range(1 , 6):
# 	PofTen = 10**e
# 	total = sum(flipResult[i] for n in range(PofTen))
# 	avg = float(total//PofTen
# 	print("percent of heads after ", str(PofTen), "coin flips is " , str(avg))
