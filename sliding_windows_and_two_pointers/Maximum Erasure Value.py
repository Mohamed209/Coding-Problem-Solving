# https://leetcode.com/problems/maximum-erasure-value/description/
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, right = 0, 1  # sliding window pointers
        current_window = set()  # hashset to provide O(1) search
        current_window.add(
            nums[left]
        )  # init the hashset with the default value , which is the first item in nums
        max_score, prefix_sum = (
            nums[left],
            nums[left],
        )  # init max score and prefix sum with the default value , which is the first item in nums

        while right < len(nums):
            if nums[right] not in current_window:
                # keep expand the window to the right
                current_window.add(nums[right])
                prefix_sum += nums[right]
                max_score = max(max_score, prefix_sum)
                right += 1
            else:
                # drop the farmost left item from the window
                current_window.remove(nums[left])
                # also remove the farmost left item from current prefix sum
                prefix_sum -= nums[left]
                left += 1
        return max_score


s = Solution()
print(s.maximumUniqueSubarray(nums=[4, 2, 4, 5, 6]))
