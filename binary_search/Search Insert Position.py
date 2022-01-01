# https://leetcode.com/problems/search-insert-position/
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left_ptr = 0
        right_ptr = len(nums)-1
        mid_idx = len(nums)//2
        while left_ptr <= right_ptr:
            if target > nums[mid_idx]:
                left_ptr = mid_idx+1
            elif target < nums[mid_idx]:
                right_ptr = mid_idx-1
            else:
                return mid_idx
            mid_idx = left_ptr+(right_ptr-left_ptr)//2
        return right_ptr+1


