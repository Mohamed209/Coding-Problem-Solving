# https://leetcode.com/problems/largest-substring-between-two-equal-characters
from typing import DefaultDict


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        occurances = DefaultDict(list)
        max_window = -1
        for i in range(len(s)):
            occurances[s[i]].append(i)
        for key in occurances:
            if len(occurances[key]) >= 2:
                max_window = max(
                    max_window, occurances[key][-1] - occurances[key][0] - 1
                )
        return max_window


s = Solution()
print(s.maxLengthBetweenEqualCharacters(s="abca"))
