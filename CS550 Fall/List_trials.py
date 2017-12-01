import random
myList = []
i = 0
while i <= 5:
	myList.append(random.randint(0 , 10))
	i += 1
myList.append(5)
del myList[0]
pizza = myList[len(myList)-1]
pizza = myList[-1]
myList[2] = 3
len(myList)
a = myList[0]
b = myList[1]
myList[0] = b
myList[1] = a
newList = []
z = 0
while z <= 100:
	newList.append(z*7)
	z += 1
num = random.randint(0, len(newList))