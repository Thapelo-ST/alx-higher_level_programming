#!/usr/bin/python3
"""
    The N queens puzzle is the challenge of placing N non-attacking queens
    on an N×N chessboard.
    This program solves the N queens problem.

    The program must and can be only be run this way.

    if not it will produce this error

    The solution is presented in this way

    Where [[r,c], [r,c]]
    r - row and  c - column
"""
import sys

def printSolution(solution):
    board = [['.' for _ in range(len(solution))] for _ in range(len(solution))]
    for row, col in solution:
        board[row][col] = 'Q'
    for row in board:
        print(row)
    print()

def isSafe(solution, row, col):
    for queen in solution:
        if queen[1] == col or queen[0] + queen[1] == row + col or queen[0] - queen[1] == row - col:
            return False
    return True

def solveNQueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    def backtrack(solution, col):
        if col == n:
            printSolution(solution)
            return
        for row in range(n):
            if isSafe(solution, row, col):
                solution.append((row, col))
                backtrack(solution, col + 1)
                solution.pop()

    backtrack([], 0)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solveNQueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
