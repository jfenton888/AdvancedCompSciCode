from time import sleep #1-5 operators needed
import os
from random import randint
import random
from random import choice as rc
global MoneyinTheBank#6-21 sets up global variables that get called in multiple functions
MoneyinTheBank = 50
global hoursTillRent
hoursTillRent = 72
global hoursofEnergy
hoursofEnergy = 24
global stars
stars = 0
global daysOfExp
daysOfExp = 1
global hoursofSleep
hoursofSleep = 0
global mark
global gamesPlayed
gamesPlayed = 0
mark = 0
targets = [' woman with an enormous handbag' , ' woman pushing a stroller that falls apart as you watch' ' scrawny man wearing an old tank top', ' woman bodybuilder with a huge wallet bulging out of her pocket' , 'stout man wearing a new suit']
targetsProfits = [ 40, 5, 15, 50, 25]# uses arrays for robbing where you can pick any spot in the first list and have corresponding values after
targetNum = [0, 0, 0, 0]

def howTo(): #esplains the rules of the game/ basics
	os.system('clear')
	print('so you want to know how to win…') 
	sleep(2)
	print('Well this is the game of life so thats up to you.')
	print('But I will suggest you start with winning some money because you only have $50 left,')
	print('and you have $500 of rent due in 2 days.')
	sleep(4)
	print('You could go to the casino, rob someone, or sell bears.')
	sleep(2)
	print('You are going to be making some risky choices to make the money you need')
	sleep(2)
	print('Each action you make will take time and energy, but you can make lots of money')
	sleep(2)
	print('The more money you try to make, the more bigger the chance you will get caught by the cops')
	sleep(2)
	print('Every day you will gain more experience, and be less likely to get caught')
	print('1 Star will originally have a certain chance of getting caught, with each extra star being more risky')

def EndSequence(): #will end the game 
	sleep(2)
	os.system('clear')
	print('This is the end, you weren\'t good enough to survive in this world')
	sleep(5)
	sys.exit()

#when either of these two are satisfied it ends the game
def CheckMoney():
	if MoneyinTheBank <= 0:
		sleep(1)
		EndSequence()
def CheckEnergy():
	if hoursofEnergy<=0:
		sleep(1)
		EndSequence()

#this code is execudetd when the code reaches a place where the cops could be investigating
def theCops(pOdds, pStars):#this is the odds that you get caught by the cops, and what happens if you do
# for odds, big numbers are good, small are bad
	global mark
	global MoneyinTheBank

	copOdds = ((pOdds * pStars) - daysOfExp) #finds the times the cop could catch the culprit(out of 100)
	yourNum = randint(0, 100) 
	if yourNum <= copOdds: #compares a random number(0,100) with the times out of 100 the cop will catch you, if rand is greater then the cops do not catch
		print('you\'ve been caught by the cops, ')
		sleep(.25)
		print('they take $25 from your wallet just becuase they can')
		MoneyinTheBank-= 25
		CheckMoney()
		oddsGetOff = float(daysOfExp) * float(pStars) * (random.random())#different function to check if the cops will percecute now that the person has been caught
		if oddsGetOff >= 5:
			print('and they are going to be procecuting you')
			EndSequence()
		else:# if caught but not procecuted you lose your money from that score
			print('but for some reason you aren\'t going to be procecuted')
			targetsProfits[mark] = 0
			return targetsProfits[mark]
	else:
		print('successful mugging!')




def robDif(): #lets you pick how hard it will be on a scale of 1 to 5 when the stars value is higher it makes it harder to not get caught, takes more energy, and gives more money
	while True:
		try:
			global robStars
			robStars = int(input('How big of a score are you looking for? \n Rank from 1 to 5 stars \n'))
			if robStars >= 1 and robStars <= 5:
				return robStars
				break
		except (ValueError, TypeError):
			print('Thats not what I asked for')

def bearDif(): #lets you pick how hard it will be on a scale of 1 to 5 when the stars value is higher it makes it harder to not get caught, takes more energy, and gives more money
	while True:
		try:
			global bearStars
			bearStars = int(input('How big of a risk do you want to take on this bear \n Rank from 1 to 5 stars \n'))
			if bearStars >= 1 and bearStars <= 5:
				return bearStars
				break
		except (ValueError, TypeError):
			print('Thats not what I asked for')

#Brian's code
def cls():
	os.system('cls' if os.name=='nt' else 'clear')
def total(hand): #This is code from a website for the aces.
    # how many aces in the hand
    aces = hand.count(11)
    # to complicate things a little the ace can be 11 or 1
    # this little while loop figures it out for you
    t = sum(hand)
    # you have gone over 21 but there is an ace
    if t > 21 and aces > 0:
        while aces > 0 and t > 21:
            # this will switch the ace from 11 to 1
            t -= 10
            aces -= 1
    return t
def Blackjack():
	global gamesPlayed
	profit = 0 # profit tracker
	cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] #Create the deck of cards
	dwin = 0  # dealer win counter
	pwin = 0  # player win counter 
	while True:
	    player = [] #create an array for the player's hand
	    player.append(rc(cards)) #adds 2 cards to the player's hand
	    player.append(rc(cards))
	    pbust = False
	    dbust = False
	    bet = 0
	    try:
	    	bet = float(input("How much money would you like to bet on this game?"))
	    except (TypeError, ValueError):
	    	print('That is not a valid number.')
	    while True:
	        tp = total(player)
	        print ("You have %s with a total value of %d" % (player, tp))
	        if tp > 21:
	            print ("You busted!")
	            pbust = True
	            break
	        elif tp == 21:
	            print ("BLACKJACK!")
	            break
	        else:
	            choice = input("Hit or Stand?")
	            if choice == 'Hit' or choice == 'hit' or choice == 'h':
	                player.append(rc(cards)) #adds cards to the players hand when they want to hit
	            else:
	                break
	    while True:
	        dealer = [] # Creates an array for dealer's hand
	        dealer.append(rc(cards))
	        dealer.append(rc(cards)) # Add two cards from cards to the dealer's hand
	        while True:
	            td = total(dealer)                
	            if td < 18: #Sets the limit to when the dealer will stand
	                dealer.append(rc(cards))
	            else:
	                break
	        print ("the dealer has %s for a total of %d" % (dealer, td))
	        if td > 21:
	            print (" The dealer busted!")
	            dbust = True
	            if pbust == False:
	                print ("You win!")
	                pwin += 1
	                profit = profit+ 2*bet
	        elif td >= tp:
	            print ("The Dealer wins!")
	            dwin += 1
	            profit = profit - bet
	        elif tp > td:
	            if pbust == False:
	                print ("You win!")
	                pwin += 1
	                profit = profit + 2*bet
	            elif dbust == False:
	                print ("The dealer wins!")
	                dwin += 1
	                profit = profit - bet
	            else:
	            	print ("Both players busted. Draw")
	        break
	    print
	    print ("Wins, player = %d  Dealer = %d" % (pwin, dwin))
	    print("Total profit = %d" % (profit))
	    gamesPlayed += 1
	    exit = input("Press Enter to continue, or Quit to exit")
	    if exit == 'quit' or exit == 'Exit' or exit == "Quit":
	        break
	    else:
	    	cls()
	print
	print ("Thanks for playing blackjack, please play another one of our games!")
	sleep(2)
	return(profit)
def Roulette():
	global gamesPlayed
	profit = 0
	ball = 0
	x = False
	ply = True
	while ply == True:
		try:
			bet = float(input("How much money would you like to bet on this game?"))
		except (ValueError, TypeError):
			print('That is not a valid number.')
			break
		Category = (input("Would you like to bet on odds, evens, or a certain number between 00 and 36.")) # make sure the player has choosen a correct choice
		try:
			x =  -1 < int(Category) < 36
		except ValueError:
			print('')
		if Category == 'odds' or Category == "Odds" or Category == "Odd" or Category == "odd":
			print("You have chosen Odds.")
			Category = "Odds"
		elif Category == 'evens' or Category == "Evens" or Category == "even" or Category == "Even":
			print("You have chosen Evens.")
			Category = "Evens"
		elif Category == '00':
			print("You have chosen 00")
			Category = -1
		elif x == True:
			print('you have chosen',Category)
		else:
			print("please select a valid Category. 00 Has been chosen for you.")
			Category = -1
			sleep(2)
		ball = randint(-1, 36)	# Check to see if the player has won
		if ball == -1 and Category == -1:
			print("The ball landed on 00, You win!")
			profit = profit + 4 * bet
		elif Category == ball:
			print("The ball landed on",ball,". You win!")
			profit = profit + 3 * bet
		elif ball // 2 == ball /2 and Category == 'Evens':
			print("The ball landed on",ball," That's an even! You win!")
			profit = profit + 1.5 * bet
		elif ball //2 != ball / 2 and Category == 'Odds':
			print("The ball landed on",ball," That's an odd! You win!")
			profit = profit + 1.5 * bet
		else:
			print("The ball landed on ",ball,". You lose.")
			profit = profit - bet
		print("You have currently made $",profit)
		sleep(1)
		gamesPlayed += 1
		exit = input("Press Enter to continue, or Quit to exit")
		if exit == 'quit' or exit == 'Exit' or exit == "Quit":
			ply = True
			break
		else:
			cls()
	print
	print ("Thanks for playing roulette, please play another one of our games!")
	return(profit)
def PlayCards():#this function and the ones labeled cls, total, Blackjack, and Roulette were adapted from the code of Bian Mcglinchy, with his permission
	cls()
	global MoneyinTheBank
	global hoursofEnergy
	gamesPlayed = 0
	MoneyinTheBank0 = MoneyinTheBank
	print('Welcome to Casino McGlinchey! Feel free to waste all of your money here')
	sleep(3)
	print("If you can make $250, you will win and extra $50 to take home!")
	sleep(2)
	input("Currently we have 2 games:")
	while (0<=MoneyinTheBank<=250):
		sleep(1)
		cls()
		print("You currently have $" + str(MoneyinTheBank))
		g = input("Which game would you like to play next? \nBlackjack, or Roulette. Or Exit \n")
		if g == 'Blackjack' or g == 'blackjack' or g == '1':
			MoneyinTheBank = MoneyinTheBank+Blackjack()
			gamesPlayed += 1
		elif g == 'Roulette' or g == 'roulette' or g == '2':
			MoneyinTheBank = MoneyinTheBank+Roulette()
			gamesPlayed += 1
		elif g == 'Exit' or g== 'exit':
			break
		else:
			input("We're sorry that there are no other games, please pick one of the above")
	if MoneyinTheBank - MoneyinTheBank0 >= 250:
		print('As you finish your game you are greeteed by Mr. McGlinchey himself.')
		sleep(2)
		print('\"Hello friend, you were really lucky today! Congratulations!\"')
		sleep(2)
		print('\"Here is your well earned $50\"')
	if MoneyinTheBank <= 0:
		print('You are thrown out to the Curb by the bouncer, where the cops are waiting to pick you up')
		print(' and throw you in a deep dark hole you will never crawl out of.')
		EndSequence()	
	else:
		hoursofEnergy-= gamesPlayed
		print('You walk home, exhasuted but happy to have money in your pocket')

#end of Brians code

def goingToBed():#lets you pick how long you want to sleep
	global hoursofSleep
	while True:
		try:
			hoursOfSleep = int(input('How long will you sleep for? \n'))
			break
		except (TypeError, ValueError):
			print(' that\'s just not right, try again')
	return hoursofSleep

def robSomeone(Rstars): 
	global MoneyinTheBank
	global hoursofEnergy
	global pChoice
	targetNum[0] = targets[randint(0,3)]#334-342 randomly assign descriptions of a person to the set personality 
	targetNum[1] = targets[randint(0,3)]#each 'target' will gve a different amount of money
	targetNum[2] = targets[randint(0,3)]#each attitude(currently doesn't change its slots) gives you the chance that you will be caught if you try to mug the person with that desctiption
	targetNum[3] = targets[randint(0,3)]
	print('you walk down to back street and can\'t help but notice 4 people that look like good targets to mug')
	print('1: a ' + targetNum[0] + ' talking on the phone to a friend')
	print('2: a ' + targetNum[1] + ' with appartment keys falling to the ground')
	print('3: a ' + targetNum[2] + ' sporting a hip holster')
	print('4: a ' + targetNum[3] + ' with a set of directions in hand, clearly lost')
	while True:
		while True:
			try:
				mark = int(input('who are you going to rob? \n')) - 1#lets you pick who you want to mug out of the 4 given, filters out anything it doesn't want
				break
			except (ValueError, TypeError):
				print('that\'s not what you really want to do is it?')
		if mark == 0:	# each attitude gives a different chance of being caught (n/100)
			pChoice = 12 
			break
		elif mark == 1:
			pChoice = 10
			break
		elif mark == 2:
			pChoice = 20
			break
		elif mark == 3:
			pChoice = 15
			break
		else:
			print('that\'s not what you really want to do is it?')
	theCops(pChoice, Rstars) #checks to see if cops can catch you
	MoneyinTheBank += (targetsProfits[mark]*Rstars)# if not caught you get more money, proportionally increased by difficulty
	hoursofEnergy -= (4 * Rstars)#if not procecuted, energy lost is proportional to difficulty
	CheckEnergy()#makes sure player doesnt have energy or money at 0
	CheckMoney()




	
	
def sellABear(Bstars): #selling bears is like reselling things on Ebay, but you will only get 3 bids with a random value between 0 and twice the amount you bought the bear for
	global MoneyinTheBank
	global hoursofEnergy
	global Rstars
	bearPrice = 50*Bstars#each level of difficulty gives you a more expensive bear
	buyingBear =input( 'Would you like to buy a bear for $' + str(bearPrice) + '? (You will get three bids on the bear you will have to accept one of these bids \n but you cannot see a bid until you have decided wether or not to accept the previous one. \n If you decline the first two, you will have to accept the third \n bids will range from 0 to twice the amount you bought the bear for) \n yes or no \n')
	if buyingBear != 'yes' and buyingBear != 'y':# gives you the choice if you want the bear after you choose difficulty, so if bear too expensive you can pass
		print('Oh thats fine this bear didn\'t like you anyway')
		sleep(5)
	else:
		MoneyinTheBank -= bearPrice#you buy the bear
		CheckMoney()
		print('Yay! You bought a bear, he\'s so happy! \n Now it\'s time to sell your new bear, and here comes your first bid')
		sleep(2)
		theCops(12, Bstars)#chance of getting caught increases by multiples of 12 based on price of bears
		#if not procecuted you can get back to the deal, starting with the first bid
		bid = randint(0,2*bearPrice)
		decision1 = input('do you want to accept the first bid of $' + str(bid) + ' for your bear? \n yes or no \n')
		if decision1 != 'yes':
			bid = randint(0,2*bearPrice)
			decision2 = input('do you want to accept the second bid of $' + str(bid) + ' for your bear? \n yes or no \n')
		if decision1 != 'yes' and decision2 != 'yes':
			bid = randint(0,2*bearPrice)
			print('the third and final bid comes in at $' + str(bid) + ' this is the third one so you have to accept it')
		MoneyinTheBank += bid #add the money you sold your bear for back into the bank
		hoursofEnergy -= (8 + Bstars/2)#buying and selling bears takes a lot of work
		CheckEnergy()

def haveADay():
	sleep(2)
	os.system('clear')#starts each day with a clean screen
	global MoneyinTheBank
	global hoursofEnergy
	dirtyJobPick=0
	print('Its morning, time to make money')#gives player a little update on where they are at with their important values
	print('you have ' + str(hoursofEnergy) + ' more hours of energy')
	print('you have $' + str(MoneyinTheBank) + ' in the bank')
	print('you\'ve got ' + str(hoursTillRent) + ' hours till the landlord knocks down your door')
	while True:
		try:#pick what you want to do at that point
			dirtyJobPick = int(input('Whatcha gonna do? \n' '1: Rob someone \n' + '2: Sell a bear \n' + '3: Head to the Casino \n'))
			(dirtyJobPick <= 1 and dirtyJobPick >= 3) == True
		except (ValueError, TypeError):
			print('You chose to do nothing and sit at home for a couple of hours, great idea')#if rsponse isn't what was specified, player loses 5 hours
			hoursofEnergy -= 5
			CheckEnergy()
		if dirtyJobPick == 1:
			robDif()	#asks dificulty you want to play in
			robSomeone(robStars) #runs the rob scene
		elif dirtyJobPick == 2:
			bearDif() #same as above
			sellABear(bearStars)
		elif dirtyJobPick == 3:
			PlayCards() #cards is hard enough, no need to make it worse
		sleep(2)
		os.system('clear')
		print('you have $' + str(MoneyinTheBank) + ' in the bank')#after doing your evil deed you can pick to rest up or do another one
		continueWithDay = input('you have ' + str(hoursofEnergy) + ' hours of energy left do you want to do something else illegal? \n')
		if continueWithDay == 'n' or continueWithDay == 'no' or continueWithDay == 'No':
			print('you walk home and fall down on your bed, ready to sleep.')
			goingToBed()
			break




howTo() #entirety of the loop function, just most is functions layered inside each other
while True:
	hoursofEnergyBefore = hoursofEnergy
	haveADay()
	timeSpent = hoursofEnergyBefore - hoursofEnergy #displays how many hours passed in that day
	hoursTillRent -= (timeSpent + hoursofSleep)
	if hoursTillRent <=0:#when the days have passed, rent is due and you have 500 take from you
		MoneyinTheBank -= 500
	hoursofEnergy += hoursofSleep*1.5
	if daysOfExp <= 50: #each day you get more experience, which helps with not getting caught, but you're more likely to get charged if you do
		daysOfExp += 1


#################################################

#uses Bian's code for the casino, I fixed a few places where it was broken, and adapted it to my needs where needed
#Palmer told me aboubt clearing the display and helped me with a few error messages I didn't get
#You helped me with a couple errors in code
