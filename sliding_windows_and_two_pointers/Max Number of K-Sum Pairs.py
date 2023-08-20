# https://leetcode.com/problems/max-number-of-k-sum-pairs
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        number = 0
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] + nums[right] == k:
                number += 1
                left += 1
                right -= 1
            elif nums[left] + nums[right] > k:
                # move right ptr to left one step
                right -= 1
            else:
                # move left ptr one step to the right
                left += 1
        return number
