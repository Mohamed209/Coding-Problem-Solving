# https://leetcode.com/problems/path-with-minimum-effort/description
# init attempt
from typing import List, Optional


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def dfs(
            row: int,
            col: int,
            prev_cell_height: int,
            visited: set,
            max_abs_dif: int,
        ) -> Optional[int]:
            if (
                row < 0
                or row >= len(heights)
                or col < 0
                or col >= len(heights[0])
                or (row, col) in visited
            ):
                return 10e9
            visited.add((row, col))
            effort = abs(
                prev_cell_height - heights[row][col]
            )  # effort to jump from cell in prev dfs call to current cell in current dfs call
            max_abs_dif = max(max_abs_dif, effort)
            if row == len(heights) - 1 and col == len(heights[0]) - 1:
                return max_abs_dif
            # standard dp approach , I really do not know which is the best path the hiker should take
            # so let us explore the four possibilities
            return min(
                dfs(row - 1, col, heights[row][col], visited, max_abs_dif),
                dfs(row + 1, col, heights[row][col], visited, max_abs_dif),
                dfs(row, col - 1, heights[row][col], visited, max_abs_dif),
                dfs(row, col + 1, heights[row][col], visited, max_abs_dif),
            )

        visited = set()
        max_abs_dif = 0
        return dfs(0, 0, heights[0][0], visited, max_abs_dif)


s = Solution()
print(s.minimumEffortPath(heights=[[1, 2, 2], [3, 8, 2], [5, 3, 5]]))
