# https://leetcode.com/problems/pacific-atlantic-water-flow/
# helper implementation : https://github.com/neetcode-gh/leetcode/blob/main/417-Pacific-Atlantic-Waterflow.py
from typing import List


class Solution:
    @staticmethod
    def dfs(r, c, heights, prev_cell, visited):
        if r < 0 or c < 0 or r == len(heights) or c == len(heights[0]) or heights[r][c] < prev_cell or (r, c) in visited:
            return
        visited.add((r, c))
        Solution.dfs(r + 1, c, heights, heights[r][c], visited)
        Solution.dfs(r - 1, c, heights, heights[r][c], visited)
        Solution.dfs(r, c + 1, heights, heights[r][c], visited)
        Solution.dfs(r, c - 1, heights, heights[r][c], visited)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific, atlantic = set(), set()
        for c in range(cols):
            Solution.dfs(0, c, heights, heights[0][c], pacific)
            Solution.dfs(rows - 1, c, heights, heights[rows - 1][c], atlantic)
        for r in range(rows):
            Solution.dfs(r, 0, heights, heights[r][0], pacific)
            Solution.dfs(r, cols - 1, heights, heights[r][cols - 1], atlantic)
        return list(atlantic.intersection(pacific))


s = Solution()
print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
