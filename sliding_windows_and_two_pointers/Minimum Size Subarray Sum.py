# https://leetcode.com/problems/minimum-size-subarray-sum/
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        min_sub_length = 1e6
        cur_window_sum = 0
        while right < len(nums):
            cur_window_sum += nums[right]
            while cur_window_sum >= target:
                min_sub_length = min(min_sub_length, right - left + 1)
                cur_window_sum -= nums[left]
                left += 1
            right += 1
        if min_sub_length == 1e6:
            return 0
        return min_sub_length


s = Solution()
print(s.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
