# https://leetcode.com/problems/maximum-total-importance-of-roads/description/
from itertools import chain
from typing import List, Counter


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        freq = dict(
            sorted(
                Counter(chain.from_iterable(roads)).items(),
                key=lambda x: x[1],
                reverse=True,
            )
        )
        max_importance = 0
        for key in freq:
            max_importance += n * freq[key]
            n -= 1
        return max_importance


s = Solution()
s.maximumImportance(n=5, roads=[[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]])
