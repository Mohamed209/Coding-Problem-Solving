# https://leetcode.com/problems/two-sum/
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsdict = {}
        for i in range(len(nums)):
            numsdict[nums[i]] = i
        for i in range(len(nums)):
            if target-nums[i] in numsdict and numsdict[target-nums[i]] > i:
                return [i, numsdict[target-nums[i]]]
