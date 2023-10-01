# https://leetcode.com/problems/longest-palindromic-subsequence/
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        @cache
        def dfs(left: int, right: int) -> int:
            if right < left:
                return 0
            if left == right:
                return 1
            if s[left] == s[right]:
                return 2 + dfs(left + 1, right - 1)
            return max(dfs(left + 1, right), dfs(left, right - 1))

        return dfs(0, len(s) - 1)
