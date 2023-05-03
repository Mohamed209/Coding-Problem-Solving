# https://leetcode.com/problems/find-the-difference-of-two-arrays/
from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1 = set(nums1)
        hash2 = set(nums2)
        res = []
        dif12 = []
        dif21 = []
        for key in hash1:
            if key not in hash2:
                dif12.append(key)
        res.append(dif12)
        for key in hash2:
            if key not in hash1:
                dif21.append(key)
        res.append(dif21)
        return res


s = Solution()
print(s.findDifference(nums1=[1, 2, 3], nums2=[2, 4, 6]))
print(s.findDifference(nums1=[1, 2, 3, 3], nums2=[1, 1, 2, 2]))
