# https://leetcode.com/problems/path-with-maximum-gold/
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(r: int, c: int, current_path: set):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or grid[r][c] == 0
                or (r, c) in current_path
            ):
                return 0
            current_path.add((r, c))
            # explore current cell 4 neighbours
            return grid[r][c] + max(
                dfs(r - 1, c, current_path),
                dfs(r + 1, c, current_path),
                dfs(r, c - 1, current_path),
                dfs(r, c + 1, current_path),
            )

        max_gold = 0
        current_path = set()
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                max_gold = max(max_gold, dfs(r, c, current_path))
                current_path.clear()
        return max_gold


s = Solution()
grid = [
    [1, 0, 7, 0, 0, 0],
    [2, 0, 6, 0, 1, 0],
    [3, 5, 6, 7, 4, 2],
    [4, 3, 1, 0, 2, 0],
    [3, 0, 5, 0, 20, 0],
]
s.getMaximumGold(grid)
