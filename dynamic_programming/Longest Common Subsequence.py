# https://leetcode.com/problems/longest-common-subsequence
from functools import cache


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def dfs(text1: str, text2: str, m: int, n: int) -> int:
            if m == 0 or n == 0:
                return 0
            if text1[m - 1] == text2[n - 1]:
                # lucky case , both last characters from every text is matched
                # let us move backwards
                return 1 + dfs(text1, text2, m - 1, n - 1)
            else:
                # os sh**t , here we go again
                # let us explore two possibilties , drop current char from text1 or text2
                return max(dfs(text1, text2, m - 1, n), dfs(text1, text2, m, n - 1))

        return dfs(text1, text2, len(text1), len(text2))
