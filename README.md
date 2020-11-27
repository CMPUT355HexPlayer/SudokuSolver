# SudokuSolver
Simple Sudoku solver/generator created in Python.
Group Members-Ranajay Sarma ,Djellza Neziri, Andrews Essilfie and Christian Arbelaez.

About

The Solver: The program will scan each cell at first and only if there exists one possibility , it will insert that number. The program will continue doing this until the puzzle gets stuck. The program then runs a backtracking DFS search to try out the possibilities and eliminates those that do not work along with its children.

Our primary aim was for code readability and simplicity over a competitive running time, although this program can solve a Sudoku puzzle in ~0.2s on average. 

The Generator: The generator fills a 9x9 2D grid with random number starting from the left most row and column and moving from there. While filling in the puzzle grid, there is a call to make sure that the number being put in the grid match the sudoku rules. After filling up the puzzle a list of indices 1-80 representing the puzzle is generated to randonmly shuffle the number of the puzzle grid. To generate the puzzle, the number in the first index of the list is removed and the generator solves then tries to solve the puzzle, this action is recursivley called until one solution is exits for the puzzle. After the puzzle is generated, the Generator outputs the puzzle in a txt file to be used by the solver.  

How to run the program

To run the solver:

    python sudoku.py Sudopuzzle.txt

To run the generator:

    python sudokuGen.py

The puzzle generator writes to a file named "Sudopuzzle.txt", with each puzzle being represented as one line of integers read from the top left to the bottom right of the grid.
