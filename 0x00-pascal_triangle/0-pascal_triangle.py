#!/usr/bin/python3
"""Returns a list of lists of integers representing the
pascal's triangle of n"""


def pascal_triangle(n):
    """algorithm for display of pascal's triangle"""
    if n == 0:
        return []
    else:
        res = [[1]]

        for i in range(n-1):
            temp = [0] + res[-1] + [0]
            row = []
            for j in range(len(res[-1]) + 1):
                row.append(temp[j] + temp[j + 1])
            res.append(row)
        return res
