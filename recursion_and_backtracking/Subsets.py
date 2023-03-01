# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def __init__(self) -> None:
        self.result = []
        self.current_path = []
        self.cache = {}

    def dfs(self, nums: List[int]) -> None:
        if len(nums) == 0:
            if tuple(self.current_path.copy()) in self.cache:
                return
            self.result.append(self.current_path.copy())
            self.cache[tuple(self.current_path.copy())] = True
            return
        for i in range(len(nums)):
            self.current_path.append(nums[i])
            self.dfs(nums[i+1:])  # take current element
            self.current_path.pop()  # not to take current element
            self.dfs(nums[i+1:])

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums)
        return self.result


s = Solution()
print(s.subsets([1, 2, 3]))
