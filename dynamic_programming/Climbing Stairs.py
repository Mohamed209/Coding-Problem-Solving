# https://leetcode.com/problems/climbing-stairs/
from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(n):
            # base case
            if n == 0:
                return 1  # there is a valid path to jump the n stairs
            if n < 0:
                return 0  # current path is not valid one
            return dfs(n - 1) + dfs(n - 2)

        return dfs(n)


s = Solution()
s.climbStairs(n=3)
