# https://leetcode.com/problems/soup-servings/description/
from functools import cache


class Solution:
    def soupServings(self, n: int) -> float:
        @cache
        def dfs(a: int, b: int):
            # first base case
            # when A only is empty first
            if a <= 0 and b > 0:
                return 1.0
            # second base case
            # when A and B are empty we need half the probability
            if a <= 0 and b <= 0:
                return 0.5
            # third base case
            # when B is empty but A not , mark this event with zero probability
            if a > 0 and b <= 0:
                return 0.0
            return (
                dfs(a - 100, b)
                + dfs(a - 75, b - 25)
                + dfs(a - 50, b - 50)
                + dfs(a - 25, b - 75)
            ) * 0.25

        if n > 4451:
            return 1.0
        return dfs(a=n, b=n)
