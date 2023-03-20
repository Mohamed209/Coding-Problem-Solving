# https://leetcode.com/problems/max-area-of-island/
from typing import List


class Solution:
    def __init__(self) -> None:
        self.visited = set()
        self.cur_island_area = 0

    def dfs(self, r, c, grid):
        # base cases to stop rcursive dfs
        if (
            r < 0
            or r >= len(grid)
            or c < 0
            or c >= len(grid[0])
            or grid[r][c] == 0
            or (r, c) in self.visited
        ):
            return 0
        self.visited.add((r, c))
        # start 4 directions dfs summing the paths
        return (
            1
            + self.dfs(r, c - 1, grid)
            + self.dfs(r, c + 1, grid)
            + self.dfs(r - 1, c, grid)
            + self.dfs(r + 1, c, grid)
        )

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                res.append(self.dfs(r, c, grid))
        return max(res)


s = Solution()
print(
    s.maxAreaOfIsland(
        grid=[
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ]
    )
)
