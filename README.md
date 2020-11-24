# SudokuSolver
Simple Sudoku solver/generator created in Python.

#About

The Solver: The program will scan each cell at first and only if there exists one possibility , it will insert that number. The program will continue doing this until the puzzle gets stuck. The program then runs a backtracking DFS search to try out the possibilities and eliminates those that do not work along with its children.

Our primary aim was for code readability and simplicity over a competitive running time, although this program can solve a Sudoku puzzle in ~0.2s on average. 

The Generator: The generator starts with an empty 9x9 grid and fills it up by iterating from the top left cell to the bottom right, and filling in the cells by trying random numbers. The generator checks if the inserted number works and if it does , the process is continued recursively. Then the full 9x9 grid is reduced down so that it becomes the start of a Sudoku puzzle. It generates a list of integers 0-80 representing the indices in the puzzle, then scrambles the order. To reduce, we try to remove the number at the first index in the list and then attempting to solve the puzzle. If there exists more than one solution, then it is not a valid Sudoku puzzle, so undo the last change. If easy puzzles are desired, then after a puzzle with a unique solution is found, algorithm stops. If difficult puzzles are wanted, then even after a valid puzzle is found, all the remaining indices are tried to see if the puzzle can be made any harder. The difficult puzzles are not only unique boards, but boards where you cannot remove any more numbers without destroying the uniqueness of the solution.

#How to run the program

To run the solver:

    python sudoku.py Sudokus.txt

To run the generator:

    python sudokuGen.py

The puzzle generator writes to a file named "SudokuPuzzles.txt", with each puzzle being represented as one line of integers read from the top left to the bottom right of the grid.
