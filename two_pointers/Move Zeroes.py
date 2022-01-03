# https://leetcode.com/problems/move-zeroes/
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_ptr = 0
        right_ptr = 1
        while(right_ptr < len(nums)):
            if nums[left_ptr] == 0 and nums[right_ptr] != 0:
                # swap the two elements
                tmp = nums[right_ptr]
                nums[right_ptr] = nums[left_ptr]
                nums[left_ptr] = tmp
                left_ptr += 1
            elif nums[left_ptr] != 0 and nums[right_ptr] != 0:
                left_ptr += 1
            elif nums[left_ptr] != 0 and nums[right_ptr] == 0:
                left_ptr += 1
            right_ptr += 1
        return nums
