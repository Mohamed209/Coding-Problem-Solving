# https://leetcode.com/problems/peak-index-in-a-mountain-array/description/
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                return mid
            # where shall we go and search now ?! , left or right subarray ?
            # from problem description left subarray is sorted descending and right ascending
            if arr[mid] < arr[mid + 1]:
                # search in right subarray
                left = mid
            else:
                right = mid
