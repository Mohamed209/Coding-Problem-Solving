# https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]  # initialize arr with first element of pref
        for i in range(1, len(pref)):
            arr.append(pref[i - 1] ^ pref[i])
        return arr


s = Solution()
s.findArray(pref=[5, 2, 0, 3, 1])
