# https://leetcode.com/problems/combination-sum/
# check ../images/howSum.png
from typing import List

# TODO : implement memoaization


class Solution:
    def __init__(self) -> None:
        self.res = []
        self.currpath = []
        self.cache = {}

    def dfs(self, candidates: List[int], target: int):
        if target in self.cache:
            return self.cache[target]
        if target < 0:
            return None
        if target == 0:
            return []
        for item in candidates:
            self.currpath.append(item)
            path = self.dfs(candidates, target-item)
            if path != None:  # valid path
                currpath_sorted = sorted(self.currpath.copy())
                if currpath_sorted not in self.res:  # unique combinations
                    self.res.append(currpath_sorted)
            self.currpath.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.dfs(candidates, target)
        return self.res


s = Solution()
print(s.combinationSum([2, 3, 5], 8))
s = Solution()
print(s.combinationSum([2, 3, 6, 7], 7))
