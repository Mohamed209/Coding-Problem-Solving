# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/description/
from typing import List


class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0  # two pointers for nums1,nums2
        max_distance = 0
        while i < len(nums1) and j < len(nums2):
            # check valid pair rule
            if nums1[i] <= nums2[j]:
                max_distance = max(max_distance, j - i)
                j += 1
            else:
                i += 1
                if i > j:
                    j = i
        return max_distance


s = Solution()
print(s.maxDistance(nums1=[55, 30, 5, 4, 2], nums2=[100, 20, 10, 10, 5]))
