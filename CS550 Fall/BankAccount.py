from random import randint
class Bank:
	def __init__(self, aNum, balance, interestR, pin, isOpen):
		self.aNum = aNum
		self.balance = balance
		self.interestR = interestR
		self.pin = pin
		self.isOpen = isOpen
	
	def stats(self):
		print('Appa Stats:')
		print('Name: ' + str(self.name))
		print('Hunger: ' + str(self.hunger))
		print('Thirst: ' + str(self.thirst))
		print('Goodness: ' + str(self.goodness))
		print('Energy: ' + str(self.energy))
		print('Fluffyness: ' + str(self.fluff))
		print(str(self.fireNationProx) + '%' + ' chance of getting caught')


	def open(self):
		self.hunger += 25
		self.thirst += 25
		self.energy -= 10
		self.fireNationProx += 10 
	def deposit(self):
		self.fireNationProx -= 20
		self.energy -= 15
		self.hunger -= 10
		self.thirst -= 15
		self.goodness -= 5
	def withdrawl(self):
		self.fireNationProx = 0
		self.energy -= 20
		self.hunger -= 15
		self.thirst -= 10
		self.fluff -=10
		self.goodness -=10
	def close(self):
		self.fluff += 50
		self.fireNationProx += 10
		self.hunger -= 5
		self.thirst -= 5


if (input('do you already have an account?')).lower == 'no'
	while True:
		try:
			bankA = Bank(randint(0,10000000000000000), int(input('how much money do you want to put in')), .05, int(input('What would you like your pin to be')), True)
			break
		except:
			print('ya know I am trying to help you so if you want an account do it right')
			if (input('do you still want to create an account?')).lower == 'no':
				break
elif (input('do you already have an account?')).lower == 'yes'

while (True):
	Appa.newAct()
	act = (str(input('What will you and Appa do?'))).lower	
	if act.find('eat')!= -1:
		Appa.eatin() 
	elif act.find('fly')!= -1:
		Appa.fly() 
	elif act.find('fight')!= -1:
		Appa.fightFireNation() 
	elif act.find('clean')!= -1:
		Appa.clean() 
	elif act.find('sleep')!= -1:
		Appa.sleep() 
	elif act.find('play')!= -1:
		Appa.playwAang() 
	Appa.stats()

