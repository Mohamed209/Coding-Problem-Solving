# https://leetcode.com/problems/contains-duplicate/
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numssorted = sorted(nums)
        for i in range(len(numssorted)-1):
            if numssorted[i] == numssorted[i+1]:
                return True
        return False
