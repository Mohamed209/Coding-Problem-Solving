# https://leetcode.com/problems/set-mismatch/description/
from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        res = []
        for key in freq:
            if freq[key] == 2:
                res.append(key)
                break
        for i in range(1, len(nums) + 1):
            if i not in freq:
                res.append(i)
                break
        return res


s = Solution()
s.findErrorNums([3, 2, 3, 4, 6, 5])
