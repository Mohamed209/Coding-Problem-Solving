# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
from math import ceil
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        """
        - the solution must be in range (1,infinity)
        - try to choose large divisor and you will possibly get very high sums > threshold
        - so let us assume solution in range(1,max(nums))
        - since we are searching in sorted range we may speed up computation using binary search
        """

        left = 1
        right = max(nums)
        res = -1
        while left <= right:
            mid = (left + right) // 2
            cursum = sum([ceil(i / mid) for i in nums])
            if cursum > threshold:
                # possibly we choosed small div value so that the sum is high, let us search in the right subarray
                left = mid + 1
            else:
                # possibly we choosed large div value so that the sum is low, let us search in the left subarray
                # or we landed a good div that matched threshold but we need minimum divisor
                res = mid
                right = mid - 1
        return res


s = Solution()
print(s.smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
print(s.smallestDivisor(nums=[44, 22, 33, 11, 1], threshold=5))
