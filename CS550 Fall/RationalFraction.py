class RationalNumber:
	def __init__(self, n, d):
		self.n = n
		self.d = d
	def __add__(self, other):
		n = self.n*other.d + self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)
	def __sub__(self, other):
		n = self.n*other.d - self.d*other.n
		d = self.d*other.d
		return RationalNumber(n, d)
	def __mul__(self, other):
		n = self.n * other.n
		d = self.d * other.d
		return RationalNumber(n, d)
	def __truediv__(self, other):
		n = self.n * other.d
		d = self.d * other.n
		return RationalNumber(n, d)
	def __str__(self):
		return ((str(self.n) + '/' + str(self.d)) + '	' + str(self.n/self.d))

def main():
	a = RationalNumber(1, 2)
	b = RationalNumber(1, 3)
	print(a)
	print(b)
	print(a+b)
	print(a-b)
	print(a*b) 
	print(a/b) 

main()