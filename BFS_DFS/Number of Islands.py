# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def __init__(self) -> None:
        self.visited = set()

    def dfs(self, r, c, grid):
        # base cases to stop rcursive dfs
        if (
            r < 0
            or r >= len(grid)
            or c < 0
            or c >= len(grid[0])
            or grid[r][c] == "0"
            or (r, c) in self.visited
        ):
            return 0
        self.visited.add((r, c))
        # start 4 directions dfs
        self.dfs(r, c - 1, grid)
        self.dfs(r, c + 1, grid)
        self.dfs(r - 1, c, grid)
        self.dfs(r + 1, c, grid)
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res += self.dfs(r, c, grid)
        return res


s = Solution()
print(
    s.numIslands(
        grid=[
            ["1", "1", "1", "1", "0"],
            ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "0", "0", "0"],
        ]
    )
)
s = Solution()
print(
    s.numIslands(
        grid=[
            ["1", "1", "0", "0", "0"],
            ["1", "1", "0", "0", "0"],
            ["0", "0", "1", "0", "0"],
            ["0", "0", "0", "1", "1"],
        ]
    )
)
