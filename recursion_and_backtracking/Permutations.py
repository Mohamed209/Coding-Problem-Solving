# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.current_path = []

    def dfs(self, nums: List[int]) -> None:
        if len(nums) == 0:
            self.result.append(self.current_path.copy())
            return
        for i in range(len(nums)):
            self.current_path.append(nums[i])
            self.dfs(nums[:i]+nums[i+1:])
            self.current_path.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums)
        return self.result


s = Solution()
print(s.permute([1, 2, 3]))
