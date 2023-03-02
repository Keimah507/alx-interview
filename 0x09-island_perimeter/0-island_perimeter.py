#!/usr/bin/python3
"""Module housing island perimeter function"""

def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid"""
    visit = set()

    def dfs(i, j):
        """
        Carries out the dfs op"""

        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0
        
        visit.add((i, j))
        perim = dfs(i, j + 1)
        perim += dfs(i + 1, j)
        perim += dfs(i, j - 1)
        perim += dfs(i - 1, j)

        return perim
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)