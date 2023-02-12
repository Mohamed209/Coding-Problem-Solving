# https://leetcode.com/problems/minimum-path-sum/
from typing import List
import math


class Solution:
    @staticmethod
    def dfs(m, n, grid, cache):
        if (m, n) in cache:
            return cache[(m, n)]
        if m < 0 or n < 0:
            return math.inf
        if m == 0 and n == 0:
            return grid[m][n]
        min_path_sum = grid[m][n] + \
            min(Solution.dfs(m-1, n, grid, cache),
                Solution.dfs(m, n-1, grid, cache))
        cache[(m, n)] = min_path_sum
        return min_path_sum

    def minPathSum(self, grid: List[List[int]]) -> int:
        cache = {}
        """
        - min path sum (grid) is grid[0][0] + which is minimum to move down so grid will shrink and starting point will be m-1,n
        or move right so also grid will shrink and starting point m,n-1 , then we recurse again
        - bottom-right cell is our target (one of the base cases) , and we can reach it from multiple paths
        starting from up-left cell , using two options down or left
        """
        return Solution.dfs(len(grid)-1, len(grid[0])-1, grid, cache)


s = Solution()
print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
