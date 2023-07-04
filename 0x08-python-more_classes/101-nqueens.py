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

def print_board(board):
    for row in board:
        print("[", end="")
        for i in range(len(row)):
            print(row[i], end="")
            if i != len(row) - 1:
                print(", ", end="")
        print("]")



def solution(board, ans, n):
    queens = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                queens.append([i, j])
    ans.append(queens)

def is_safe(row, col, board, n):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i = row
    j = col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    ans = []
    solve_nqueens_helper(board, 0, ans, n)
    return ans

def solve_nqueens_helper(board, row, ans, n):
    if row == n:
        solution(board, ans, n)
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 1
            solve_nqueens_helper(board, row + 1, ans, n)
            board[row][col] = 0

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print_board(solution)

