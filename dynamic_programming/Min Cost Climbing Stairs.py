# https://leetcode.com/problems/min-cost-climbing-stairs/description
from functools import cache
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def dfs(i: int):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i + 1), dfs(i + 2))

        return min(
            dfs(0), dfs(1)
        )  # You can either start from the step with index 0, or the step with index 1.


s = Solution()
print(s.minCostClimbingStairs(cost=[10, 15, 20]))
print(s.minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
