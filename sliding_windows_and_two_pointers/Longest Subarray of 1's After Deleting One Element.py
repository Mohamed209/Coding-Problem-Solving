# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_ones = 0
        nums_str = "".join([str(i) for i in nums])
        ones = nums_str.split("0")
        if len(ones) == 1:
            return len(nums) - 1
        lens = [len(one) for one in ones]
        for i in range(len(lens) - 1):
            max_ones = max(max_ones, lens[i] + lens[i + 1])
        return max_ones


s = Solution()
print(s.longestSubarray([0, 0, 0]))
print(s.longestSubarray([1, 1, 1]))
print(s.longestSubarray(nums=[1, 1, 0, 1]))
print(s.longestSubarray(nums=[0, 1, 1, 1, 0, 1, 1, 0, 1]))
