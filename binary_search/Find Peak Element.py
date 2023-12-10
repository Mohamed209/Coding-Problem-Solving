# https://leetcode.com/problems/find-peak-element/description/
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            if mid > 0 and nums[mid - 1] > nums[mid]:
                right = mid - 1
            elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
                left = mid + 1
            else:
                return mid


s = Solution()
s.findPeakElement(nums=[1, 2, 1, 3, 5, 6, 4])
