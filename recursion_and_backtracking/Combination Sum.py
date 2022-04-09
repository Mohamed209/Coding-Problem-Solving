# https://leetcode.com/problems/combination-sum/
from copy import deepcopy
from typing import List


class Solution:
    @staticmethod
    def dfs(target, candidates, current_combs, res, idx):
        if target == 0:
            res.append(deepcopy(current_combs))
            return
        for i in range(idx, len(candidates)):
            if candidates[i] > target:
                break
            current_combs.append(candidates[i])
            Solution.dfs(target-candidates[i],
                         candidates, current_combs, res, i)
            current_combs.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        current_combs = []
        res = []
        Solution.dfs(target, sorted(candidates), current_combs, res, 0)
        return res