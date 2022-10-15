# https://leetcode.com/problems/maximum-subarray/
# ref : https://www.youtube.com/watch?v=86CQq3pKSUw
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_max, global_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            current_max = max(nums[i], nums[i]+current_max)
            if current_max > global_max:
                global_max = current_max
        return global_max