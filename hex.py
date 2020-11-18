from os import system, name
import random

#GLOBAL VARIABLES

#4x4 board
brd = ["a","b","c","d",
		"f","g","h","i",
		 "j","k","l","m",
		  "n","p","q","r"]

#Moves players can still make
availableMoves = ["1","1","1","1",
					"1","1","1","1",
		 			  "1","1","1","1",
		  			    "1","1","1","1"]

moves = []

#Is the game still going?
game = True


#FUNCTIONS

#Prints board and current moves to screen
def showBoard(brd):
	print(" ")
	print(brd[0]+" "+brd[1]+" "+brd[2]+" "+brd[3])
	print(" "+brd[4]+" "+brd[5]+" "+brd[6]+" "+brd[7])
	print(" "+" "+brd[8]+" "+brd[9]+" "+brd[10]+" "+brd[11])
	print(" "+" "+" "+brd[12]+" "+brd[13]+" "+brd[14]+" "+brd[15])
	print(" ")

#Takes the user's move and adjusts the board and available moves.
def processMove(brd, x):
	moved = x in moves

	if (moved):
		print(" ")
		print("INVALID MOVE!")
	else:
		y = brd.index(x)
		brd[y] = "X"
		availableMoves[y] = "0"
		moves.append(x)

# Clears terminal display.
def clear(): 
# from: https://www.geeksforgeeks.org/clear-screen-python/

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 



#MAIN PROGRAM:
clear()
print("*************************************")
print("Welcome to 4x4 Hex!")


while(game):
	showBoard(brd)
	x = input("Which letter do you want to move to: ")
	processMove(brd,x)

	








			