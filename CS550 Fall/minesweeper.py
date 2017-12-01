from random import randint
rows = 0 
colm = 0
bombs = 0
crows = 1
ccolm = 1
bombleft = 0
bombStatus = 0
spaces = 0
while True:
	try:
		rows = int(input('How many rows')) + 2
		colm = int(input('How many columns')) + 2
		bombs = int(input('How many bombs'))
	except (ValueError, TypeError): 
		print('no I only want numbers ')
		break
	bombleft = bombs
	gameBoard = [[0]*rows for i in range(rows)]
	print(gameBoard)
	while crows <= rows-2:
		if crows == 0:
				crows += 1
		ccolm = 1
		while ccolm <= (colm-2):
			if ccolm == 0:
				ccolm += 1
			if bombleft > 0:
				spacesLeft = ((rows-2)*(colm-2)-spaces)	
				print(spacesLeft)					
				isBomb = randint(1 , spacesLeft)				
			else:
				isBomb = -1
			if isBomb >= bombleft:
				bombStatus = '*'
				bombleft -= 1
			else:
				bombStatus = '-1'
			print('isBomb=' + str(isBomb))
			print('bombleft=' + str(bombleft))
			print('crows=' + str(crows))
			print ('ccolm=' + str(ccolm))
			gameBoard[crows][ccolm] = bombStatus
			print(gameBoard)
			spaces +=1
			ccolm += 1
		crows +=1
	break
crows = 1
ccolm = 1
while(True):
	print('in whiletrue')
	while crows <= rows-1:
		ccolm = 1
		while ccolm <= colm-1: 
			print('in bomb checker')
			bombsAround = 0
			if gameBoard[crows][ccolm] == '-1':
				try:
					int(gameBoard[crows-1][ccolm+1])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows][ccolm+1])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows+1][ccolm+1])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows-1][ccolm])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows+1][ccolm])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows-1][ccolm-1])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows-1][ccolm-1])
				except:
					bombsAround +=1
				try:
					int(gameBoard[crows-1][ccolm-1])
				except:
					bombsAround +=1
				print(bombsAround)
				gameBoard[crows][ccolm] = bombsAround
			ccolm += 1
		crows += 1
	break

print(' ______________')
print(('|  ') + str(gameBoard) + (' | '))