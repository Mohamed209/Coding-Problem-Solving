# https://leetcode.com/problems/k-closest-points-to-origin/
import math
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        return sorted(points, key=lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2))[:k]


s = Solution()
print(s.kClosest(points=[[1, 3], [-2, 2]], k=1))
print(s.kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))