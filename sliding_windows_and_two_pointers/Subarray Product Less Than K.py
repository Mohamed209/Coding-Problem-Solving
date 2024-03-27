# https://leetcode.com/problems/subarray-product-less-than-k/description/?envType=daily-question&envId=2024-03-27
# TLE :D
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        cnt = 0
        window_prod = 1
        while left < len(nums):
            print("current window", nums[left : right + 1])
            window_prod *= nums[right]
            if window_prod < k:
                right += 1
                cnt += 1
            else:
                left += 1
                right = left
                window_prod = 1
            if right >= len(nums):
                left += 1
                right = left
                window_prod = 1
        return cnt


s = Solution()
s.numSubarrayProductLessThanK(nums=[10, 5, 2, 6], k=100)
