# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gropus = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in gropus:
                gropus[key].append(s)
            else:
                gropus[key] = [s]
        return list(gropus.values())
