# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    @staticmethod
    def dfs(row, col, grid):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] in ['0', '2']:
            # water or visited or out of bounds
            return
        grid[row][col] = '2'  # mark as visited
        # search in all four directions horizontal and vertical
        Solution.dfs(row-1, col, grid)
        Solution.dfs(row+1, col, grid)
        Solution.dfs(row, col-1, grid)
        Solution.dfs(row, col+1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        no_of_lands = 0
        # visit every cell , complexity O(rows*cols)
        for r in range(rows):
            for c in range(cols):
                # call the dfs starting from current cell
                if grid[r][c] == '1':
                    Solution.dfs(r, c, grid)
                    no_of_lands += 1
        return no_of_lands
