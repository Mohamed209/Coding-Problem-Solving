# https://leetcode.com/problems/assign-cookies/description/
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        gptr, sptr = 0, 0
        max_score = 0
        while gptr < len(g) and sptr < len(s):
            if s[sptr] >= g[gptr]:
                # current cookie size >= current child greed
                max_score += 1
                gptr += 1  # move to satisfy next child greed
            sptr += 1
        return max_score
