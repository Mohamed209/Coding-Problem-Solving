# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/description/
from typing import List
import heapq


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # first approach
        nums.sort()
        return (nums[-1] - 1) * (nums[-2] - 1)
        # second approach
        # heapq.heapify([-n for n in nums])
        # firstmax, secondmax = heapq.nlargest(2, nums)
        # return (firstmax - 1) * (secondmax - 1)


s = Solution()
print(s.maxProduct(nums=[3, 4, 5, 2]))
