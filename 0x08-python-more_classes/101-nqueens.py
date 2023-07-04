#!/usr/bin/python3
"""
    The N queens puzzle is the challenge of placing N non-attacking queens
    on an N×N chessboard.
    This program solves the N queens problem.

    The program must and can be only be run this way.
    ./101-nqueens.py 6 any size greater than 8 will not be accepted
    if not it will produce this error

    The solution is presented in this way
    user@machines1$ ./101-nqueens.py 6
    [[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
    [[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
    [[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
    [[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
    Where [[r,c], [r,c]]
    r - row and  c - column
"""
import sys


def print_board(board):
    """
    prints the board
    :param board: is the size of the board maybe a 4x4 board
    :return: the board with the solution
    """
    for row in board:
        print("[", end="")
        for idx in range(len(row)):
            print(row[idx], end="")
            if idx != len(row) - 1:
                print(", ", end="")
        print("]")


def solution(board, answer, n):
    """
    try to find all possible solution of where to place queens where they
    will not capture each other
    :param board: is the size of the board maybe a 4x4 board
    :param answer: is the number of solutions provided
    :param n: sets the size of the board 4 means the board will be a 4x4
    :return: the solutions provided
    """
    queens = []
    for k in range(n):
        for j in range(n):
            if board[k][j] == 1:
                queens.append([k, j])
    answer.append(queens)


def is_safe(row, col, board, n):
    """
    checks if the queen is safe or not
    :param row: row where the queen is in
    :param col: checks if the queen is there as well
    :param board: is the size of the board maybe a 4x4 board
    :param n: sets the size of the board
    :return: the safety of the queen
    """
    # Check if there is a queen in the same column
    for index in range(row):
        if board[index][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    index = row
    j = col
    while index >= 0 and j >= 0:
        if board[index][j] == 1:
            return False
        index -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    index = row
    j = col
    while index >= 0 and j < n:
        if board[index][j] == 1:
            return False
        index -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    solves the solution if is safe did produce an answer
    :param n: sets the size of the board
    :return: the answer to the prompted problem
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    ans_list = []
    solve_nqueens_helper(board, 0, ans_list, n)
    return ans_list


def solve_nqueens_helper(board, row, answ, n):
    """
    if the solve_nqueens did not help this function will run
    :param row: is the row on the board
    :param board: is the size of the board maybe a 4x4 board
    :param answ: is the number of solutions provided
    :param n: sets the size of the board 4 means the board will be a 4x4
    :return: the solutions provided
    """
    if row == n:
        solution(board, answ, n)
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 1
            solve_nqueens_helper(board, row + 1, answ, n)
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
        ans = []
        for i in range(len(solution)):
            ans.append(solution[i])
            if (i + 1) % N == 0:
                print(ans)
                ans = []
        if ans:
            print(ans)
