#https://leetcode.com/problems/successful-pairs-of-spells-and-potions
from bisect import bisect_left
from typing import List
import math


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        potions.sort()
        res = []
        for spell in spells:
            bileft = bisect_left(potions, math.ceil(success / spell))  # binary search
            res.append(len(potions) - bileft)
        return res


s = Solution()
print(s.successfulPairs(spells=[3, 1, 2], potions=[8, 5, 8], success=16))