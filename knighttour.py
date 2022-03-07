#!/usr/bin/env python
#
#Jenny Zhong
#

import sys
import random
import copy

board = []

kmoves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))

temp_choices = []

def main():
	global rows
	global columns 
	global attempts
	
	if len(sys.argv) > 3:
		rows = int(sys.argv[1])
		columns = int(sys.argv[2])
		attempts = int(sys.argv[3])
	
	else: 
		print ("There must be 3 integer input arguments")
		sys.exit(1)
	for i in range(0, rows):
		board.append(columns*[0])
	
		PossibleMoves(0,0,1,attempts) #starting at (1,1)
	 
		PrintBoard()

		PrintOutcome()
	 
def InGridAndEmpty(ty,tx):  # check if position is within board and empty
    return ty>=0 and tx>=0 and ty<rows and tx<columns \
        and board[ty][tx] == 0

def PossibleMoves(y,x,start,tries):
        board[y][x] = start
        for k in range(0,tries):
                #kmoves = ((2,1), (1,2), (-1,2), (-2,1), (-2,-1), (-1,-2), (1,-2), (2,-1))
                for k in range(0,8):
                    for move in kmoves: # check possible moves on board and make sure it is empty
                        ty,tx = y+move[0], x+move[1]
                        if InGridAndEmpty(ty,tx):
                                temp_choices.insert(ty,tx)
                                print (temp_choices)
								#print '[%s]' % ', '.join(map(str, temp_choices))
                               # start += 1
                               # board[ty][tx] = start
                               # y = ty
                               # x = tx

	
def PrintOutcome():
        if 0  in [m for n in board for m in n]:
                print ("Failure") # prints failed if there is square left unvisited.
        else:
                print ("Success")


def PrintBoard(): # print the board
    scale = len(str(rows*columns))
    print(rows*("+" + scale*"-") + "+")
    for line in board:
        for elem in line:
            sys.stdout.write("|%*d" % (scale,elem))
        print("|\n"+columns*("+" + scale*"-") + "+")

if __name__ == "__main__":
    main()
             

