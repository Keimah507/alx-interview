#!/usr/bin/python3
"""Rotates an n x n 2D matrix clockwise"""

def rotate_2d_matrix(matrix):
    """Rotate the matrix"""
    l, r = 0, len(matrix) - 1
    
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            #save the top left
            topLeft = matrix[top][l + i]

            #move bottom left to top left
            matrix[top][l + i] = matrix[bottom - i][l]

            #move bottom right to bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            #move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            #move top left into top right
            matrix[top + i][r] = topLeft

        r -= 1
        l += 1
