# https://leetcode.com/problems/climbing-stairs/
from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        cache = {}
        cache[1] = 1
        cache[2] = 2
        for i in range(3, n+1):
            cache[i] = cache[i-1]+cache[i-2]
        return cache[n]
