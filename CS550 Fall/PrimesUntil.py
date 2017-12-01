import sys
try:
	maxNum = int(input('This program will give you every prime number lower than the integer you input \n'))
except (TypeError, ValueError):
	print('Nope, just not what I asked for')
	sys.exit()
posFact = 1
numOfFact = 0
thePrimes = []
num = 1
while num <= maxNum:
	while posFact <= (num):
	 	if num % posFact == 0:
	 		numOfFact += 1
	 	posFact += 1
	if numOfFact <= 2:
		thePrimes.append(num)
	posFact = 1
	numOfFact = 0
	num += 1
thePrimes.remove(1)
print(thePrimes)