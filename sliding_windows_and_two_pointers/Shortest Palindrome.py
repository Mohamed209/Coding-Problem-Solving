# https://leetcode.com/problems/shortest-palindrome/
from typing import List


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def is_pali(s: List):
            return s[::-1] == s

        if len(s) == 0 or len(s) == 1 or is_pali(s):
            return s
        sl = list(s)
        i = 0
        j = len(sl) - 1 - i
        while True:
            sl.insert(i, sl[j])
            if is_pali(sl):
                return "".join(sl)
            i += 1
