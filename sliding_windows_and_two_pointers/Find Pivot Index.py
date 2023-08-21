# https://leetcode.com/problems/find-pivot-index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_nums_sum = sum(nums)
        right_sum = all_nums_sum - nums[0]
        left_sum = 0
        i = 0
        while i < len(nums):
            if right_sum == left_sum:
                return i
            else:
                left_sum += nums[i]
                i += 1
                if i == len(nums):
                    break
                right_sum -= nums[i]
        return -1


s = Solution()
print(s.pivotIndex([-1, -1, 0, 1, 1, 0]))
