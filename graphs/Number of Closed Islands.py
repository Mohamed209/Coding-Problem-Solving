from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        R = len(grid) - 1
        C = len(grid[0]) - 1

        def Ok(r, c):
            return 0 <= r <= R and 0 <= c <= C

        def dfs(r, c):
            if Ok(r, c):
                if grid[r][c] == 0:
                    grid[r][c] = 1
                    right = dfs(r, c + 1)
                    down = dfs(r + 1, c)
                    up = dfs(r - 1, c)
                    left = dfs(r, c - 1)
                    return left and up and down and right
                return True
            return False

        for r in range(R + 1):
            for c in range(C + 1):
                if grid[r][c] == 0 and dfs(r, c):
                    ans += 1

        return ans
