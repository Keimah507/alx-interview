#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that
solves the N queens problem.

Usage:
    nqueens N If the user called the program with the wrong number of arguments, print Usage: nqueens N,
    followed by a new line, and exit with the status 1 where N must be an integer
    greater or equal to 4

    If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1

    If N is smaller than 4,
    print N must be at least 4, followed by a new line, and exit with the status 1

    The program should print every possible solution to the problem One solution
    per line Format: see example You don’t have to print the solutions in a
    specific order

    You are only allowed to import the sys module
    """
import sys


def valid_pos(solution, pos):
    """
    Function that verifies if the position is valid
    """
    for queen in solution:
        if queen[1] == pos[1]:
            return False
        if (queen[0] + queen[1]) == (pos[0] + pos[1]):
            return False
        if (queen[0] - queen[1]) == (pos[0] - pos[1]):
            return False
    return True


def solve_queens(row, n, solution):
    """
    Function that finds the solution recursively, from the root down
    """
    if row == n:
        print(solution)
    else:
        for col in range(n):
            pos = [row, col]
            if valid_pos(solution, pos):
                solution.append(pos)
                solve_queens(row + 1, n, solution)
                solution.remove(pos)


def main(n):
    """
    Main function
    """
    solution = []
    """ From root(0) down(n) """
    solve_queens(0, n, solution)


if __name__ == '__main__':
    # Validate the arguments from OS
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)
    try:
        i = int(sys.argv[1])
    except BaseException:
        print('N must be a number')
        sys.exit(1)
    num = int(sys.argv[1])
    if num < 4:
        print('N must be at least 4')
        sys.exit(1)

    # Calling the main function
    main(i)
