# https://leetcode.com/problems/reducing-dishes/description/
from typing import List
from functools import cache


class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        @cache
        def dfs(index: int, time_stamp: int):
            # recursion base case
            if index >= len(satisfaction):
                return 0
            # we have two options
            # 1- prepare the dish
            prepare = satisfaction[index] * time_stamp + dfs(index + 1, time_stamp + 1)
            # 2- skip current dish
            skip = dfs(index + 1, time_stamp)
            return max(prepare, skip)

        return dfs(index=0, time_stamp=1)


s = Solution()
print(s.maxSatisfaction(satisfaction=[-1, -8, 0, 5, -9]))
