# https://leetcode.com/problems/wiggle-sort-ii/description/
from typing import List
import heapq


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        # sorted copy of original array
        array = sorted(nums)
        
        # take the bigest elements and insert them into odd positions
        for i in range(1, len(nums), 2):
            nums[i] = array.pop()
        
        # insert remaining elements into even positions
        for i in range(0, len(nums), 2):
            nums[i] = array.pop()


s = Solution()
print(s.wiggleSort(nums=[1, 5, 1, 1, 6, 4]))
print(s.wiggleSort(nums=[1, 3, 2, 2, 3, 1]))
