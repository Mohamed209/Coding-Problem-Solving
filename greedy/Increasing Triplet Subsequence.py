# https://leetcode.com/problems/increasing-triplet-subsequence/description/
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float("inf")
        for i, n in enumerate(nums):
            if min1 < min2 < n:
                return True
            elif n < min1:
                min1 = n
            elif min1 < n < min2:
                min2 = n
        return False


s = Solution()
nums = [20, 100, 10, 12, 5, 13]
s.increasingTriplet(nums)
nums = [0, 4, 2, 1, 0, -1, -3]
s.increasingTriplet(nums)
