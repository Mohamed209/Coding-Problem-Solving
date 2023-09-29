# https://leetcode.com/problems/monotonic-array
from itertools import pairwise


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        pairs = list(pairwise(nums))
        return all(x[0] <= x[1] for x in pairs) or all(x[0] >= x[1] for x in pairs)
