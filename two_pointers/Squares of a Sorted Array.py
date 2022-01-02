# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_ptr = 0
        right_ptr = len(nums)-1
        res = []
        while(left_ptr <= right_ptr):
            sqr_left = nums[left_ptr]**2
            sqr_right = nums[right_ptr]**2
            if sqr_left<sqr_right:
                res.insert(0,sqr_right)
                right_ptr-=1
            else:
                res.insert(0,sqr_left)
                left_ptr+=1
        return res