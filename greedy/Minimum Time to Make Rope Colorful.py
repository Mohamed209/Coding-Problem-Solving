# https://leetcode.com/problems/minimum-time-to-make-rope-colorful
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left, right = 0, 1
        mincost = 0
        while right < len(colors):
            if colors[left] != colors[right]:
                time = sorted(neededTime[left:right])
                for t in range(
                    len(time) - 1
                ):  # greedy approach is to target remove all ballons with small needed time first , but leave only the one with largest needed time
                    mincost += time[t]
                left = right
            right += 1
        # handle case when from some index left until right out of bound all chars are the same
        if colors[left] == colors[right - 1]:
            time = sorted(neededTime[left:right])
            for t in range(len(time) - 1):
                mincost += time[t]
        return mincost


s = Solution()
s.minCost(colors="abaac", neededTime=[1, 2, 3, 4, 5])
s.minCost(colors="aabaa", neededTime=[1, 2, 3, 4, 1])
