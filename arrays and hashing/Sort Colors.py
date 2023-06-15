# https://leetcode.com/problems/sort-colors/
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = {0: 0, 1: 0, 2: 0}
        for num in nums:
            freq[num] += 1
        reds, whites, blues = freq[0], freq[1], freq[2]
        nums[:reds] = [0] * reds
        nums[reds : reds + whites] = [1] * whites
        nums[reds + whites :] = [2] * blues
