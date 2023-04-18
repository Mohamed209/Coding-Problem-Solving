# https://leetcode.com/problems/majority-element/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = 0
        # scan every contigous window of the same numbers
        # there is two options
        # 1- while scanning if current window size exceeds len(nums)//2 then just return current element and do not continue scan
        # 2- finished scanning one window and it happend to exceed len(nums)//2 so return current element
        window_size = 0
        while right < len(nums):
            if nums[left] == nums[right]:
                window_size += 1
                if window_size > len(nums) // 2:
                    return nums[left]
            else:
                if window_size > len(nums) // 2:
                    return nums[left]
                window_size = 0  # new nindow
                left = right
                continue
            right += 1
        return -1


s = Solution()
print(s.majorityElement([2, 2, 1, 1, 1, 2, 2]))
print(s.majorityElement([3, 2, 3]))
