#!/usr/bin/python3
"""Module housing island perimeter function"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid"""
    visit = set()

    def dfs(k, l):
        """
        Carries out the dfs op"""

        if k >= len(grid) or l >= len(grid[0]) or k < 0 or l < 0 or grid[k][l] == 0:
            return 1
        if (k, l) in visit:
            return 0

        visit.add((k, l))
        perim = dfs(k, l + 1)
        perim += dfs(k + 1, l)
        perim += dfs(k, l - 1)
        perim += dfs(k - 1, l)

        return perim

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
