#https://leetcode.com/problems/jump-game
from functools import cache
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        @cache
        def dfs(index: int) -> bool:
            # one base case poosible if the jump is very powerful , and i am out of bounds
            if index >= len(nums):
                return False
            # base case if I reached the last index
            if index == len(nums) - 1:
                return True
            # possible paths / options try different jump values until you reach max jumps
            possible_jupms = nums[index]
            for jumb in range(1, possible_jupms + 1):
                if dfs(index + jumb):
                    return True
            return False

        return dfs(index=0)


s = Solution()
print(s.canJump(nums=[2, 3, 1, 1, 4]))
