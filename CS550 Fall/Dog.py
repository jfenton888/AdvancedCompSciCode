class Dog:
	def __init__(self, name, hunger, thirst):
		self.name = name
		self.hunger = hunger
		self.thirst = thirst
		self.goodness = 100
		self.energy = 25
	
	def stats(self):
		print('Dog Stats:')
		print('Name: ' + str(self.name))
		print('Hunger: ' + str(self.hunger))
		print('Thirst: ' + str(self.thirst))
		print('Goodness: ' + str(self.goodness))
		print('Energy: ' + str(self.energy))

	def fetch(self):
		if (self.energy >= )
		self.goodness += 5
		self.energy -= 5
		self.hunger -= 5
		self.thirst -=10

mydog1 = Dog('Puffie', 50, 50)
mydog1.stats()
mydog1.fetch()
mydog1.stats()
