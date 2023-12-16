# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        pd = Counter(p)
        for i in range(len(s) - len(p) + 1):
            if s[i] in p and Counter(s[i : i + len(p)]) == pd:
                res.append(i)
        return res


s = Solution()
print(s.findAnagrams("baa", "aa"))
print(s.findAnagrams("cbaebabacd", "abc"))
print(s.findAnagrams("abab", "ab"))
print(s.findAnagrams("baa", "aa"))
print(s.findAnagrams("abab", "ab"))
