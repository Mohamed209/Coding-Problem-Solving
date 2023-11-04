# https://leetcode.com/problems/wiggle-sort-ii/description/
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        # sorted copy of original array
        array = sorted(nums)
        # take the biggest elements and insert them into odd positions
        for i in range(1, len(nums), 2):
            nums[i] = array.pop()
        # insert lowest elements into even positions
        for i in range(0, len(nums), 2):
            nums[i] = array.pop()
