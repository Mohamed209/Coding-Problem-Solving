# https://leetcode.com/problems/number-of-zero-filled-subarrays/
from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        # let us count how many subarrays with consecutive zeros lies in nums !?
        zeros_windows = []
        left = 0
        while left < len(nums):
            if nums[left] != 0:
                left += 1
            else:
                right = left
                while right < len(nums) and nums[right] == 0:
                    right += 1
                zeros_windows.append(right - left)
                left = right

        # now for every window length of n in zeros_windows , the total subarray follow below equation
        # n * (n + 1) // 2
        def count_subarrys(n):
            return n * (n + 1) // 2

        res = 0
        for window in zeros_windows:
            res += count_subarrys(window)
        return res


s = Solution()
print(s.zeroFilledSubarray(nums=[0, 0, 0, 2, 0, 0]))
print(s.zeroFilledSubarray(nums=[1, 3, 0, 0, 2, 0, 0, 4]))
print(s.zeroFilledSubarray(nums=[2, 10, 2019]))
print(s.zeroFilledSubarray(nums=[2019]))
print(s.zeroFilledSubarray(nums=[0]))
print(s.zeroFilledSubarray(nums=[0, 1, 0]))
