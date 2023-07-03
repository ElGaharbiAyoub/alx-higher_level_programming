#!/usr/bin/python3

import sys


def nqueens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def is_safe(board, row, col):
        # Check if a queen can be placed at the given
        #  position without attacking any other queens
        for i in range(row):
            if board[i] == col or board[i] - i == col - row or \
                    board[i] + i == col + row:
                return False
        return True

    def solve_nqueens(board, row):
        # Base case: all queens have been placed, so print the solution
        if row == N:
            print([[i, board[i]] for i in range(N)])
            return

        # Try placing the queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                solve_nqueens(board, row + 1)

    board = [-1] * N
    solve_nqueens(board, 0)


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

nqueens(N)
