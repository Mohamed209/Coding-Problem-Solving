# https://leetcode.com/problems/max-consecutive-ones-iii/
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        zeros_count = 0
        max_length = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros_count += 1
            while zeros_count > k:
                if nums[left] == 0:
                    zeros_count -= 1
                left += 1
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length


s = Solution()
print(s.longestOnes(nums=[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
