# https://leetcode.com/problems/number-of-enclaves/description/
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(row: int, col: int) -> int:
            if (
                (row, col) in visited
                or row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or grid[row][col] == 0
            ):
                return 0
            visited.add((row, col))
            # recursive dfs in all 4 adjacent directions
            return (
                1
                + dfs(row - 1, col)
                + dfs(row + 1, col)
                + dfs(row, col - 1)
                + dfs(row, col + 1)
            )

        rows, cols = len(grid), len(grid[0])
        total_land_cells = 0
        # count total ones in grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_land_cells += 1
        # what if all cells are zeros ? , lucky we are , let us return 0 now
        if total_land_cells == 0:
            return 0
        visited = set()
        result = 0
        for r in range(rows):
            for c in range(cols):
                # if we are at border cell with value 1 and not visited from any previous dfs traversal
                # let us start dfs
                if (
                    (r, c) not in visited
                    and grid[r][c] == 1
                    and (c in [0, cols - 1] or r in [0, rows - 1])
                ):
                    result += dfs(r, c)
        return total_land_cells - result
