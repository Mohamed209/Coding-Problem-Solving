# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions
from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        res = [[] for _ in range(max(freq.values()))]
        for key in freq:
            for occ in range(freq[key]):
                res[occ].append(key)
        return res


s = Solution()
print(s.findMatrix(nums=[1, 3, 4, 1, 2, 3, 1]))
