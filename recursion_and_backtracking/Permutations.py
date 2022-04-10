# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    @staticmethod
    def dfs(nums, path, res):
        if len(nums) == 0:
            res.append(path)
            return
        for i in range(len(nums)):
            Solution.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        Solution.dfs(nums, path, res)
        return res
