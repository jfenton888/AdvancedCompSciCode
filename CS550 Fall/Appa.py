from random import randint
class Sky_Bison:
	def __init__(self, name, hunger, thirst, goodness, energy, fluff, fireNationProx):
		self.name = name
		self.hunger = hunger
		self.thirst = thirst
		self.goodness = goodness
		self.energy = energy
		self.fluff = fluff
		self.fireNationProx = fireNationProx
	
	def stats(self):
		print('Appa Stats:')
		print('Name: ' + str(self.name))
		print('Hunger: ' + str(self.hunger))
		print('Thirst: ' + str(self.thirst))
		print('Goodness: ' + str(self.goodness))
		print('Energy: ' + str(self.energy))
		print('Fluffyness: ' + str(self.fluff))
		print(str(self.fireNationProx) + '%' + ' chance of getting caught')


	def eatin(self):
		self.hunger += 25
		self.thirst += 25
		self.energy -= 10
		self.fireNationProx += 10 
	def fly(self):
		self.fireNationProx -= 20
		self.energy -= 15
		self.hunger -= 10
		self.thirst -= 15
		self.goodness -= 5
	def fightFireNation(self):
		self.fireNationProx = 0
		self.energy -= 20
		self.hunger -= 15
		self.thirst -= 10
		self.fluff -=10
		self.goodness -=10
	def cleanOff(self):
		self.fluff += 50
		self.fireNationProx += 10
		self.hunger -= 5
		self.thirst -= 5
	def sleep(self):
		self.energy += 50
		self.fireNationProx += 10
		self.hunger -= 5
		self.thirst -= 5
	def playwAang(self):
		self.goodness += 40
		self.energy -= 5
		self.hunger -= 5
		self.thirst -=10
		self.fireNationProx += 20
	def newAct(self):
		self.fluff -= 5
		self.goodness -= 5
		if(randint(0,100) <= self.fireNationProx):
			Appa.fightFireNation()
			if (self.energy <= 0 or self.hunger <= 0 or self.thirst <= 0):
				print('you lost Appa')
		if(self.energy <= 0):
			Appa.sleep()
Appa = Sky_Bison('Appa', 50, 50, 75, 50, 100, 50)
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

