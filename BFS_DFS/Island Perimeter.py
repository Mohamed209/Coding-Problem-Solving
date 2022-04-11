# https://leetcode.com/problems/island-perimeter/
from typing import List


class Solution:
    @staticmethod
    def dfs(r, c, grid, visited):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == 0:
            return 1
        if (r, c) in visited:
            return 0
        visited.add((r, c))
        return Solution.dfs(r, c-1, grid, visited)+Solution.dfs(r-1, c, grid, visited)+Solution.dfs(r, c+1, grid, visited)+Solution.dfs(r+1, c, grid, visited)

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:  # start dfs only from land cell
                    return Solution.dfs(r, c, grid, visited)
        return 0


s = Solution()
grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(s.islandPerimeter(grid))
