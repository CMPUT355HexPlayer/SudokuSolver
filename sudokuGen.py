import random

# reference = https://github.com/Reberog/Sudoku-Generator/blob/main/Code.txt


# Allowing the user/player to select the level of difficulty for the solver
# Then a sudoku puzzle is generated 

def checkValid(grid, rowX, colY, numB):
    """This function is to check if the sudoku puzzle being generated is a valid puzzle
    It takes the puzzle grid, the row, col and number generated in the non valid puzzle 
    grid and check it here"""
    valid = True

    # checking every row and column holds the correct value
    for x in range(9):
        if grid[x][colY] == numB:
            valid = False
            break

    for y in range(9):
        if grid[rowX][y] == numB:
            valid = False

    rowSection = rowX // 3
    colSection = colY // 3
    for x in range(3):
        for y in range(3):
            if grid[rowSection * 3 + x][colSection * 3 + y] == numB:
                valid = False
                break
    return valid


print("Select difficulty level")
difficulty = {
    1 : "Beginner",
    2 : "Intermediate",
    3 : "Advanced"
}

for key, value in difficulty.items():
    print(str(key) + "  " + value)

while True:
    levelInput = input("Please select difficulty level of puzzle to generate: ")
    try:
        if int(levelInput) in difficulty.keys():
            if int(levelInput) == 1:
                q = 22
            elif int(levelInput) == 2:
                q = 14
            else:
                q = 8
        break
    except ValueError:
        print("Please enter a number that is between 1 and 3!")

# generate a 2d array to store the puzzle 
puzzle = [[0 for x in range(9)] for y in range(9)]

# now generate random values and assign it to the grid
for i in range(q):
    row = random.randrange(9)
    col = random.randrange(9)
    num = random.randrange(1, 10)

    # check to see if the number in the puzzle grid is valid  and not empty(the grid contains only zeroes)
    while not checkValid(puzzle, row, col, num) or puzzle[row][col] != 0:
        row = random.randrange(9)
        col = random.randrange(9)
        num = random.randrange(1, 10)
    puzzle[row][col] = num

# output the puzzle grid
for i in range(len(puzzle)):
    if i % 3 == 0 and i != 0:
        print("- - - - - - - - - - - - - - ")
    for j in range(len(puzzle)):
        if j % 3 == 0 and j != 0:
            print(" | ", end = "")

        if j == 8:
            print(puzzle[i][j])
        else:
            print(str(puzzle[i][j]) + " ", end = "")

# Format the 2D array into one line of integers and then store in a txt file 
# to be used by the sudoku solver.py
fileOutput = open("Sudopuzzle.txt", "w")
toOneline = ""
for i in range(len(puzzle)):
    for j in range(len(puzzle)):
        toOneline += str(puzzle[i][j])
fileOutput.write(toOneline)
fileOutput.close()