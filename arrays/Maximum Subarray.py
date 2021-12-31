# https://leetcode.com/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        subarr_sum = nums[0]

        for i in range(1, len(nums)):
            subarr_sum = max(nums[i], nums[i] + subarr_sum)
            ans = max(ans, subarr_sum)
        return ans
