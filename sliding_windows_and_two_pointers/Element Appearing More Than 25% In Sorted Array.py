# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        left, right = 0, 0
        tw_five_percent = int(len(arr) * 0.25)
        while right < len(arr):
            if arr[left] != arr[right]:
                # check current window size
                if right - left > tw_five_percent:
                    return arr[left]
                else:
                    left = right  # start new window
            right += 1  # as long as arr[left]==arr[right] keep expand the window size
        return arr[left]


s = Solution()
s.findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10])
s.findSpecialInteger(arr=[1, 1])
