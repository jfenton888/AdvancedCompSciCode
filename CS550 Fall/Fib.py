b = int(input('nums'))
c = 0
def fib(n):
	if n < 2:
		return n
	else:
		return (fib(n-1) + fib(n-2))
while c <= b:
	print (fib(c))
	c += 1


#num = int(input(''))
#def facto(num):
#	if num < 2:
#		return 1
#	else:
#		return facto(num-1)*num
#print(facto(num))

