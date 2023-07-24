# https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx_tofill = 0
        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                continue
            nums[idx_tofill] = nums[i]
            idx_tofill += 1
        nums[idx_tofill] = nums[len(nums) - 1]
        print(nums)
        return idx_tofill + 1


s = Solution()
print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
