import math
try:
	num = list(input(''))
except:
	exit()
x = 0
while x<len(num):
	num[x] = int(num[x])
	x +=1
sumNum = (sum(num))
print(sumNum)


