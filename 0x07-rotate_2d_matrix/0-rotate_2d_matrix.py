#!/usr/bin/python3
"""Rotates an n x n 2D matrix clockwise"""


def rotate_2d_matrix(matrix):
    """Rotate the matrix"""
    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            # save the top left
            topLeft = matrix[top][left + i]

            # move bottom left to top left
            matrix[top][left + i] = matrix[bottom - i][left]

            # move bottom right to bottom left
            matrix[bottom - i][left] = matrix[bottom][right - i]

            # move top right into bottom right
            matrix[bottom][right - i] = matrix[top + i][right]

            # move top left into top right
            matrix[top + i][right] = topLeft

        right -= 1
        left += 1
