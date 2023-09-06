# https://leetcode.com/problems/edit-distance
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dfs(word1: str, word2: str, m: int, n: int) -> int:
            if m == 0:
                return n
            if n == 0:
                return m
            if word1[m - 1] == word2[n - 1]:
                return dfs(word1, word2, m - 1, n - 1)
            else:
                return 1 + min(
                    dfs(word1, word2, m - 1, n),
                    dfs(word1, word2, m, n - 1),
                    dfs(word1, word2, m - 1, n - 1),
                )

        return dfs(word1, word2, len(word1), len(word2))
