#!/usr/bin/env python3
""" Computes minimum operations needed in a text editor that 
results in exactly n H characters in the file, where n is a number and H
 is a single character"""


def minOperations(n):
    """
    Compute minimum number of operations for copy all and paste in the text editor

    Args:
        n: input value
    Return: the sum of the operations
    """
    if n < 2:
        return 0
    factor_list = []
    i = 1
    while n != 1:
        i += 1
        if n % i == 0:
            while n % i == 0:
                n /= i
                factor_list.append(i)
    return sum(factor_list)
