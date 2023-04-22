# https://leetcode.com/problems/jump-game/
from typing import List


# one approach DP + MEMO (TLE)
class Solutiondp:
    def __init__(self) -> None:
        self.cache = {}

    def dfs(self, startidx: int, nums: List[int]) -> bool:
        if startidx == len(nums) - 1:
            # base case , I mamanged to find a jump path to land me on the final element
            return True
        if nums[startidx] == 0 or startidx >= len(nums):
            # base case , landing on zero will block me from moving forward
            # base case if I take a jump to moves me out of bound
            return False
        numstuple = tuple(nums[startidx:])
        if numstuple in self.cache:
            return self.cache[numstuple]
        jumps = nums[startidx]
        for j in range(1, jumps + 1):
            res = self.dfs(startidx + j, nums)
            if res:
                self.cache[numstuple] = True
                return True
        self.cache[numstuple] = False
        return False

    def canJump(self, nums: List[int]) -> bool:
        return self.dfs(0, nums)


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        destination_idx = len(nums) - 1  # last index
        jump_power_idx = destination_idx - 1  # index before last index
        while jump_power_idx >= 0:
            # can current jump_power boost me to reach destination ?
            jump_power = nums[jump_power_idx]
            if jump_power >= destination_idx - jump_power_idx:
                # this is perfect ! , sub problem solved
                # let us move the pointers to the left
                if jump_power_idx == 0:
                    # perfect ! perfect , I already reached the end of the array
                    return True
                jump_power_idx -= 1
                destination_idx = jump_power_idx + 1
            else:
                # let us try previous jump power
                jump_power_idx -= 1
        return False


s = Solution()
print(s.canJump([3, 2, 1, 0, 4]))
print(s.canJump([3, 2, 2, 0, 4]))
print(s.canJump([2, 3, 1, 1, 4]))
