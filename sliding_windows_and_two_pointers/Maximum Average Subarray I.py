# https://leetcode.com/problems/maximum-average-subarray-i/
import math
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k >= len(nums):
            return sum(nums) / len(nums)
        max_avg_subarray = -math.inf
        prev_window_sum = None
        left = 0
        right = 0
        while right < len(nums):
            if (
                right - left + 1 == k
            ):  # we are inside a sliding window with target size k
                if not prev_window_sum:
                    # first time to compute sliding window sum
                    prev_window_sum = sum(nums[left : right + 1])
                else:
                    # using previous windows sums to create next windows sums , simply by discard nums[left-1] and add nums[right]
                    prev_window_sum = prev_window_sum - nums[left - 1] + nums[right]
                max_avg_subarray = max(max_avg_subarray, prev_window_sum / k)
                left += 1
            right += 1
        return max_avg_subarray


s = Solution()
nums = [[1, 12, -5, -6, 50, 3], [1, 2, 3], [5]]
ks = [4, 5, 1]
for num, k in zip(nums, ks):
    print(s.findMaxAverage(num, k))
