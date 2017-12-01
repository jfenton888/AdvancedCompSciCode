import os
import sys
from random import randint
import numpy as np

rowsmaze = 4
colsmaze = 10
rowstotal = rowsmaze + 2
colstotal = colsmaze + 2
rowsinit = rowstotal
colsinit = colstotal

samprowinit = []
board = []
frontierpoints = [] 

recentincluded =[rowstotal-1,1]
x = rowstotal-1
y = 1

global localInd
localInd = []

def addIndex(x, y):
    board[x][y] = 'I_'
    addFrontiers(x, y)
    frontierpoints.remove((x, y))
    checkInd(x-1, y) 
    checkInd(x+1, y)
    checkInd(x, y-1)
    checkInd(x, y+1)
    pickInd = localInd[(randint(0, len(localInd)-1))]
    if x - pickInd[0] == 1:
        board[x][y] = 'ID'
    if x - pickInd[0] == -1:
        board[x][y] = 'IU'
    if y - pickInd[1] == 1:
        board[x][y] = 'IL'
    if y - pickInd[1] == -1:
        board[x][y] = 'IR'
    while (len(localInd)) > 0:
        localInd.pop(0)


def checkInd(x,y):

    try:
        #if x != 0 and x != rowstotal-1 and y != 0 and y != colstotal-1:
        if 'I' in board[x][y]:
            localInd.append((x,y))

    except:
        return

def addFrontiers(x, y):
    #check if x-1,y is indexd or in actual board
    checkState(x-1, y) 
    checkState(x+1, y)
    checkState(x, y-1)
    checkState(x, y+1)

def checkState(x, y):
    try:
        if x != 0 and x != rowstotal-1 and y != 0 and y != colstotal-1:
            if 'I' not in board[x][y] and board[x][y] != 'FF':
                if (x,y) not in frontierpoints:
                    frontierpoints.append((x,y))
                    board[x][y] = 'FF'
    except:
        return

def removePaths():
	for y in range (len(maze[0])):
		for x in range(len(maze)):
			if maze[x][y] == 'IU':
				maze[x][y] = '  '
				maze[x+1][y] = '  '
			if maze[x][y] == 'IL':
				maze[x][y] = '  '
				maze[x][y-1] = '  '
			if maze[x][y] == 'ID':
				maze[x][y] = '  '
				maze[x-1][y] = '  '
			if maze[x][y] == 'IR':
				maze[x][y] = '  '
				maze[x][y+1] = '  '
'''
1. declare start point
2. full size grid
3. declare frontier points based on current included (start point)
4. randomly select one frontier point and add to included
5. check everything around that point for included points, if there are more than one, randomly select which one is its root
6. declare that frontier point as included in respect to its root. (ID, IU, IL, IR)
7. create new frontier points which are non-included, non-zero points
8. repeat until
9. complete

?. build a wall
'''


board = [['0 ']*colstotal for i in range(rowstotal)]


board[rowstotal-1][1] = 'I-'
addFrontiers(x,y)

#while (not mapped):
count = 0
while count < ((rowstotal-2)*(colstotal-2)):
    newIndex = frontierpoints[randint(0,len(frontierpoints)-1)]
    addIndex(newIndex[0],newIndex[1])
    count += 1
board[0][colstotal-2] = 'IU'

z = rowstotal
while z > 0:
    print(board[z-1])
    z -=1 



maze = [['0 ']*((colstotal * 2) - 3)for i in range((rowstotal * 2) - 1)]
print('\n')

for y in range (0 , len(maze[0]), 2):
    for x in range (0, len(maze), 2):
    	maze[(x)][(y-1)] = board[int(x*.5)][int(y*.5)]

for y in range (1, len(maze[0])-1):
	for x in range (1, len(maze)-1, 2):
		maze[(x)][(y)] = ('==')

for y in range (2, len(maze[0])-2, 2):
	for x in range (1, len(maze)-1): 
		maze[(x)][(y)] = ('||')

removePaths()
z = (len(maze))
w = (len(maze[0]))
while z > 0:
		while w > 0:
			pass print(maze[z-1][])   
    z -=1 
#print ('\n'.join(''.join(*zip(*row)) for row in grid))






