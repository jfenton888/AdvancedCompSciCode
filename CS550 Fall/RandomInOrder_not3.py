import random 
fullList = []
orderList = []
i = 0
while i <= 9:
	fullList.append(random.randint(0,100))
	i += 1
v = 0
while v<= 9:
	x = min(fullList)
	orderList.append(x)
	fullList.remove(x)
	if x % 3 ==0:
		orderList.remove(x)
	v += 1
print(orderList)
