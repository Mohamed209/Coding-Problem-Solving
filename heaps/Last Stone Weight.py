# https://leetcode.com/problems/last-stone-weight/
from typing import List

from sortedcontainers import SortedList

"""
since we are dealing with too many frequent remove / insert operations
ordinary list is not optimized for such behavior
so we use  SortedList optimized for too many frequent remove / insert operations
"""


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = SortedList(stones, lambda x: -x)
        while len(stones) > 1:
            x, y = stones[1], stones[0]
            stones.pop(0)
            stones.pop(0)
            if x == y:
                continue
            else:
                stones.add(y - x)
        if stones == []:
            return 0
        return stones[0]


s = Solution()
print(s.lastStoneWeight(stones=[2, 7, 4, 1, 8, 1]))
print(s.lastStoneWeight(stones=[1]))
print(s.lastStoneWeight(stones=[]))
