# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10**9 + 7

        @cache
        def count(n, target):
            if n == 0:
                return 1 if target == 0 else 0
            possible_ways = 0
            for face in range(1, k + 1):
                possible_ways = (possible_ways + count(n - 1, target - face)) % mod
            return possible_ways

        return count(n, target)
