# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
import heapq
from math import floor
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """
        - we need greedy approach to keep remove stones from the piles with max stones
        - assume you have removed stones x from piles y you will need to rearrange piles to keep sorted order
        - max heap is best suited for this problem
        """
        piles_heap = []
        for item in piles:
            heapq.heappush(piles_heap, -item)
        while k > 0:
            heapq.heappush(piles_heap, floor(heapq.heappop(piles_heap) / 2))
            k -= 1
        return sum([-1 * i for i in piles_heap])


s = Solution()
print(s.minStoneSum(piles=[10000], k=10000))
print(s.minStoneSum(piles=[5, 4, 9], k=2))
print(s.minStoneSum(piles=[4, 3, 6, 7], k=3))
print(s.minStoneSum(piles=[1], k=1e4))
