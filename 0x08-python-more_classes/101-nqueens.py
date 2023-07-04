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

def printSolution(board):
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def isSafe(board, row, col):
    # Check if there is a queen in the same row
    if 1 in board[row]:
        return False

    # Check upper diagonal on left side
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check lower diagonal on left side
    i, j = row, col
    while i < len(board) and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1

    return True

def solveNQUtil(board, col, solutions):
    if col >= len(board):
        solutions.append([pos for pos, value in enumerate(board)])
        return

    for row in range(len(board)):
        if isSafe(board, row, col):
            board[row][col] = 1
            solveNQUtil(board, col + 1, solutions)
            board[row][col] = 0

def solveNQueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * n for _ in range(n)]
    solutions = []
    solveNQUtil(board, 0, solutions)

    for solution in solutions:
        printSolution(solution)

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
