# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_ptr = 0
        right_ptr = len(numbers)-1
        while(left_ptr != right_ptr):
            if numbers[left_ptr]+numbers[right_ptr] > target:
                # move right_ptr to the left
                right_ptr -= 1
            elif numbers[left_ptr]+numbers[right_ptr] < target:
                # ove left_ptr to the right:
                left_ptr += 1
            else:
                return [left_ptr+1, right_ptr+1]
