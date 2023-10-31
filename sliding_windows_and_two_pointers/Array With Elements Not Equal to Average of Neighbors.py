# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/description/
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        left, right = 0, len(nums) - 1
        while left <= right:
            if left == right:
                res.append(nums[left])
                break
            res.extend([nums[left], nums[right]])
            left += 1
            right -= 1
        return res


s = Solution()
print(s.rearrangeArray(nums=[1, 2, 3, 4, 5]))
