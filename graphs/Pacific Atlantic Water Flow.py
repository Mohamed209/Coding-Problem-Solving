# https://leetcode.com/problems/pacific-atlantic-water-flow/
from typing import List


class Solution:
    def dfs(
        self, visited: set, r: int, c: int, heights: List[List[int]], start_point: int
    ):
        if (
            c < 0
            or c >= len(heights[0])
            or r < 0
            or r >= len(heights)
            or ((r, c)) in visited
            or start_point > heights[r][c]
        ):
            return
        visited.add((r, c))
        start_point = heights[r][c]
        self.dfs(visited, r, c + 1, heights, start_point)
        self.dfs(visited, r, c - 1, heights, start_point)
        self.dfs(visited, r + 1, c, heights, start_point)
        self.dfs(visited, r - 1, c, heights, start_point)

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pvisited = set()
        avisited = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        for r in range(ROWS):
            self.dfs(
                pvisited, r, 0, heights, 0
            )  # starting from pacific left , what are cells that can flow the water to atlantic right ?
            self.dfs(
                avisited, r, COLS - 1, heights, 0
            )  # starting from atlantic right, what are cells that can flow the water to pacific left ?
        for c in range(COLS):
            self.dfs(
                pvisited, 0, c, heights, 0
            )  # starting from pacific up , what are cells that can flow the water to atlantic down ?
            self.dfs(
                avisited, ROWS - 1, c, heights, 0
            )  # starting from atlantic down, what are cells that can flow the water to pacific up ?
        return list(avisited.intersection(pvisited))


s = Solution()
print(
    s.pacificAtlantic(
        [
            [1, 2, 2, 3, 5],
            [3, 2, 3, 4, 4],
            [2, 4, 5, 3, 1],
            [6, 7, 1, 4, 5],
            [5, 1, 1, 2, 4],
        ]
    )
)
