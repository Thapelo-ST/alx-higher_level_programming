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


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]

    N = len(board)

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row, col
    while i >= 0 and j < N:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(N):
    # Solve the N-queens problem

    def backtrack(board, row):
        # Backtracking function to find all solutions

        if row == N:
            # Found a valid solution, print the board
            solution = []
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        solution.append([i, j])
            print(solution)
            return

        for col in range(N):
            if is_safe(board, row, col):
                # Place a queen at board[row][col]
                board[row][col] = 1
                backtrack(board, row + 1)
                # Remove the queen for backtracking
                board[row][col] = 0

    # Check if N is a valid integer
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    # Check if N is at least 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    backtrack(board, 0)


if __name__ == '__main__':
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line argument
    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
