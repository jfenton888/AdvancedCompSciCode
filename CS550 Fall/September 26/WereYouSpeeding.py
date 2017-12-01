import random

numGen = float(random.uniform(50 , 100))
YoBDay = int(random.uniform(1 , 366))
theDayOfToday = int(random.uniform(1 , 366))
print("you were going ", end='')
print(numGen , end='')
print("mph, but the speed limit was 60!")
if YoBDay == theDayOfToday:
	numGen = numGen - 5
	print("However, by looking at your license I see it is your birthday")
if numGen >= 61:
	print("You're gonna get a ticket Buck-o")
	if numGen <= 80:
		print("Its only a small one though, consider yourself lucky")
	else:
		print("I'm gonna smack you with a big one, just to teach you a lesson")
else:
	print("so, great work get back on your way")
