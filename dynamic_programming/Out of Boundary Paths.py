# https://leetcode.com/problems/out-of-boundary-paths
class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        memo = {}

        def solve(i, j, mi):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if mi == 0:
                return 0
            if (i, j, mi) in memo:
                return memo[(i, j, mi)]
            row = [0, 1, 0, -1]
            col = [1, 0, -1, 0]
            total_paths = 0
            for a in range(4):
                r, c = i + row[a], j + col[a]
                total_paths += solve(r, c, mi - 1)
            memo[(i, j, mi)] = total_paths
            return total_paths

        return solve(startRow, startColumn, maxMove) % (10**9 + 7)
