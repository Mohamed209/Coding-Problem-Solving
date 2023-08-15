# https://leetcode.com/problems/non-decreasing-array
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        descending_steps = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                descending_steps += 1
                if descending_steps > 1:
                    return False
                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
        return True
