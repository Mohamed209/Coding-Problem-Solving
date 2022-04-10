# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    @staticmethod
    def dfs(nums, res, path):
        if path not in res:
            res.append(path)
        for i in range(len(nums)):
            Solution.dfs(nums[i+1:], res, path+[nums[i]])

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr_path = []
        Solution.dfs(sorted(nums), res, curr_path)
        return res


s = Solution()
print(s.subsetsWithDup([1, 2, 2]))
