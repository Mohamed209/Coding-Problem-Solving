from bisect import bisect_left
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         res.append(i)
        #     elif nums[i] > target:
        #         break
        # if len(res) == 0:
        #     return [-1, -1]
        # return [res[0], res[-1]]
        
        def binarySearch(a, x):
            i = bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return i
            else:
                return -1

        start = binarySearch(nums, target)
        end = start
        for i in range(start + 1, len(nums)):
            if nums[i] == target:
                end = i
            else:
                break
        return [start, end]


s = Solution()
s.searchRange([5, 7, 7, 8, 8, 10], 8)
