import random
import sudoku

# Allowing the user/player to select the level of difficulty for the solver
# Then a sudoku puzzle is generated 

def checkValid(grid, rowX, colY):
    """
    This function is to check if the sudoku puzzle being generated is a valid puzzle
    It takes the puzzle grid, the row, col and number generated in the non valid puzzle 
    grid and check it here.
    And returns True if the given cell is valid 
    """

    rowSection = rowX // 3
    colSection = colY // 3

    # Checking row and column and ignore blank spots
    for x in range(9):
        if grid[rowX][x] != 0 and x != colY and grid[rowX][x] == grid[rowX][colY]:
            return False
        if grid[x][colY] != 0 and x != rowX and grid[x][colY] == grid[rowX][colY]:
            return False

    for x in range(3):
        for y in range(3):
            newRow = x + rowSection * 3
            newCol = y + colSection * 3
            if grid[newRow][newCol] != 0 and newRow != rowX and newCol!= colY\
                and grid[newRow][newCol] == grid[rowX][colY]:
                return False

    return True

def populateGridPuzzle(puzzle, row, col):
    """
    Takes in the 2D puzzle grid populatiing it with random numbers
    Then calls the checkVlaid function on the puzzle grid to make sure
    the number works. If none of the number works, it sets the
    puzzle grid to blank and returns False.
    """
    if row == 8 and col == 8:
        usedNum = sudoku.valid_nbrs(puzzle, row, col)
        puzzle[row][col] = usedNum.index(0)
        return True

    if col == 9:
        row += 1
        col = 0

    temp = list(range(1, 10))
    random.shuffle(temp)
    # Fill in the puzzle with the number
    for i in range(9):
        puzzle[row][col] = temp[i]
        if checkValid(puzzle, row, col):
            if populateGridPuzzle(puzzle, row, col + 1):
                return True
    puzzle[row][col] = 0
    return False

def solvePuzzle(copyPuzzle, row, col):
    """
    Recursively solves a copy of the puzzle with backtracing DFS algorithm
    and return the number of solution found starting from row 0 and col 0.
    """
    numSolution = 0

    # checking of we reached the last cell without any error, 
    # meaning there is a solution
    if row == 8 and col ==8:
        return numSolution + 1

    if col == 9:
        row += 1
        col = 0

    if copyPuzzle[row][col] == 0:
        usedNum = sudoku.valid_nbrs(copyPuzzle, row, col) # checks if the number in already used in the grid puzzle
        # if 0 is not in usedNum then the number is already being used
        if 0 not in usedNum: 
            return 0
        
        # if 0 is in usedNum then the number is possible to be added to the puzzle
        while 0 in usedNum:
            copyPuzzle[row][col] = usedNum.index(0)
            usedNum[usedNum.index(0)] = 1
            numSolution += solvePuzzle(copyPuzzle, row, col + 1)

        copyPuzzle[row][col] = 0
        return numSolution
    
    numSolution+= solvePuzzle(copyPuzzle, row, col + 1)
    return numSolution

def puzzleDifficulty(puzzle, difficulty):
    """
    Takes in a complete puzzle, and removes the numbers in the puzzle 
    and run the solvePuzzle function on the puzzle
    """
    indicies = list(range(81)) # generate indicies 1- 80 representing the indicies in the puzzle
    random.shuffle(indicies)

    while indicies:
        row = indicies[0] // 9
        col = indicies[0] % 9
        temp = puzzle[row][col]
        puzzle[row][col] = 0
        indicies = indicies[1:]

        copyPuzzle = [l[:] for l in puzzle]

        sudoku.first_try(copyPuzzle)

        for lines in copyPuzzle:
            if 0 in lines:
                numSolution = solvePuzzle(copyPuzzle, 0, 0)
                if numSolution > 1:
                    puzzle[row][col] = temp
                    # if the user want an easy puzzle, we return the puzzle 
                    # else we make it hard by taking out more numbers in the puzzle
                    if difficulty == 1:
                        return
                break
    return

def outputGrid (puzzle):
    """
    Takes in the puzzle generated and outputs for the user to see what the puzzle looks like
    """
    for i in range(len(puzzle)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")
        for j in range(len(puzzle)):
            if j % 3 == 0 and j != 0:
                print(" | ", end = "")

            if j == 8:
                print(puzzle[i][j])
            else:
                print(str(puzzle[i][j]) + " ", end = "")

def convertToOneline(puzzle):
    """ 
    Takes in the puzzle grid and format the 2D array into one line of integers 
    and then store in a txt file 
    to be used by the sudoku solver.py 
    """
    toOneline = ""
    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            toOneline += str(puzzle[i][j])
    return toOneline + "\n"



def main():
    fileOutput = open("Sudopuzzle.txt", "w")

    print("Select difficulty level")
    difficulty = {
        1 : "Beginner",
        2 : "Advanced"
    }

    for key, value in difficulty.items():
        print(str(key) + "  " + value)

    while True:
        levelInput = input("Please select difficulty level of puzzle to generate: ")
        howManyPuzzle  = input("Please enter how many puzzle to generate: ")
        try:
            if int(levelInput) in difficulty.keys() and int(howManyPuzzle):
                howManyPuzzle = int(howManyPuzzle)
                if int(levelInput) == 1:
                    q = 1
                else:
                    q = 2
            break
        except ValueError:
            print("Please enter a number!")

    # generate a 2d array to store the puzzle 
    # checks if the puzzle is valid, and if valid
    # stores the puzzle in a text file and outputs it for
    # it for the user to try and solve it before using sudoku.py to solve it
    for _ in range(howManyPuzzle):
        puzzle = [[0] * 9 for _ in range(9)]
        populateGridPuzzle(puzzle, 0, 0)
        puzzleDifficulty(puzzle, q)
        convertPuzzle = convertToOneline(puzzle)
        outputGrid(puzzle)
        print("\n")
        fileOutput.write(convertPuzzle)
    fileOutput.close()

if __name__ == "__main__":
    main()