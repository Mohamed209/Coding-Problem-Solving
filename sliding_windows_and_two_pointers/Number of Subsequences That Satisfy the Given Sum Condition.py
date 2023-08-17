# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        count = 0
        mod = 10**9 + 7
        while left <= right:
            if nums[left] + nums[right] > target:
                # since array is sorted and the sum > target , let us move right pointer to left
                right -= 1
            else:
                # now we are 100% sure that the subarray lies between nums[left:right]
                count += pow(2, right - left, mod)
                left += 1
        return count % mod
