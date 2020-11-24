import fileinput

def display_puzzle(s):
    """
    Formats the Sudoku puzzle currently in a 2D list into
    a grid with lines separating the blocks for readability
    """
    for row in range(9):
        for col in range(9):
            print(s[row][col], end=' ')
            if col+1 == 3 or col+1 == 6:
                print(" | ", end=' ')
        if row+1 == 3 or row+1 == 6:
            print("\n" + "-"*25, end=' ')
        print()
    print()

def test_cell(s, row, col):
    """
    Given a Sudoku puzzle s, row, and column number, return a list which represents
    the valid numbers that can go in that cell. 0 = possible, 1 = not possible
    """
    used = [0]*10
    used[0] = 1
    block_row = row // 3
    block_col = col // 3

    # Row and Column
    for m in range(9):
        used[s[m][col]] = 1
        used[s[row][m]] = 1

    # Square
    for m in range(3):
        for n in range(3):
            used[s[m + block_row*3][n + block_col*3]] = 1

    return used

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
                used = test_cell(s, row, col)
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
        used = test_cell(s, row, col)
        if 0 in used:
            s[row][col] = used.index(0)
        return True

    if col == 9:
        row = row+1
        col = 0

    if s[row][col] == 0:
        used = test_cell(s, row, col)
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

        print("="*30)
        nbrs = nbrs[9:]

if __name__ == "__main__":
    main()
