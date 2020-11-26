import fileinput
import time
# from colorama import init
# init()

# from colorama import Fore, Back, Style

def display_puzzle(s):
    """
    Formats the Sudoku puzzle currently in a list into a sudoku grid
    Replaces the 0s of the puzzle with ' ' for visualization purposes
    Changes the colors of the text
    """

    print('+---' + "+----"*8 + "+")
    
    for row in range(9):
        for col in range(9):
            if (s[row][col] == 0):
                print(' ', ' ', end='')
            else:    
                print(' ', s[row][col], end='')

            if ((col == 2) | (col == 5) | (col == 8)): 
                print(" |", end='')
            else:
                print("  ", end='')

        if ((row == 2) | (row == 5) | (row == 8)): 
            print("\n" + "+---"
            + "+----"*8 + "+")
        else:
            print("\n" + "   ")

    print()

def valid_nbrs(s, row, col):
    """
    Valid_nbrs returns a list of all the numbers from 0-9 that can go into the cell
    given its row and col position as well as the s grid.
    The value is 0 if the number can go into the cell, 1 if not.
    """

    corner_row = row // 3
    corner_col = col // 3
    used_cells = [0]*10
    used_cells[0] = 1

    # Row and Column
    for val in range(9):
        used_cells[s[val][col]] = 1
        used_cells[s[row][val]] = 1

    # Square
    for c in range(3):
        for r in range(3):
            used_cells[s[c + corner_row*3][r + corner_col*3]] = 1

    return used_cells

def first_try(s):
    """
    Given a Sudoku puzzle, try to solve the puzzle by iterating through each
    cell and determining the possible numbers in that cell. If only one possible
    number exists, fill it in and continue till the puzzle is stuck.
    """
    puzzle_stuck = False

    while not puzzle_stuck:
        puzzle_stuck = True
        # Iterate through the Sudoku puzzle
        for row in range(9):
            for col in range(9):
                used = valid_nbrs(s, row, col)
                # If there is more than one possibility
                if used.count(0) != 1:
                    continue

                for m in range(1, 10):
                    # If current cell is empty and there is only one possibility
                    # then fill in the current cell
                    if s[row][col] == 0 and used[m] == 0:
                        s[row][col] = m
                        puzzle_stuck = False
                        break

def dfs(s, row, col):
    """
    Given a Sudoku puzzle, solve the puzzle by recursively performing backtracking DFS
    which tries out the possible solutions and eliminating
    invalid tries and all the possible cases arising from those invalid tries
    """
    if row == 8 and col == 8:
        used = valid_nbrs(s, row, col)
        if 0 in used:
            s[row][col] = used.index(0)
        return True

    if col == 9:
        row = row+1
        col = 0

    if s[row][col] == 0:
        used = valid_nbrs(s, row, col)
        for i in range(1, 10):
            if used[i] == 0:
                s[row][col] = i
                if dfs(s, row, col+1):
                    return True

        # If it reached here it means we tried 1-9 without success
        s[row][col] = 0
        return False

    return dfs(s, row, col+1)

def main():
    start = time.time()
    puzzle_no = 0
    text = ""

    # Get all the lines from the input
    for line in fileinput.input():
        line = ' '.join(line.split())
        text += line

    # Keep only the numbers from the input
    text = [int(i) for i in text if i.isdigit()]

    # Separate the numbers for 9x9 sudoku puzzles
    nbrs = [list(text[i:i+9])for i in range(0, len(text), 9)]

    
    while(len(nbrs) >= 9):  
        puzzle_no += 1 
        sdku = nbrs[:9]
        print("Puzzle {f}: ".format(f=puzzle_no))

        # Display a 9x9 puzzle
        display_puzzle(sdku)

        first_try(sdku)
        if (any(0 in i for i in sdku)):
                dfs(sdku, 0, 0)

        print("Solution:")
        display_puzzle(sdku)

        print("="*45 + "\n")
        nbrs = nbrs[9:]

    print("The program took {:.2f} seconds to solve {} puzzle(s).".format(time.time() - start, puzzle_no))        

if __name__ == "__main__":
    main()
