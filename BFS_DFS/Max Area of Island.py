# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def dfs(i, j):
            if i == len(grid) or i < 0 or j == len(grid[0]) or j < 0 or (i, j) in visited or grid[i][j] == 0:
                return 0
            visited.add((i, j))
            return 1+(dfs(i-1, j)+dfs(i+1, j)+dfs(i, j-1)+dfs(i, j+1))
        # first we have to visit every cell in the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    # apply dfs on this cell
                    max_area = max(dfs(i, j), max_area)
        return max_area


s = Solution()
print(s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [
    0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]))
