# https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
from typing import List
from collections import deque


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        q = deque(piles)
        my_loot = 0
        while q:
            q.popleft()  # Alice turn
            my_loot += q.popleft()  # my turn
            q.pop()  # Bop turn , give him the smallest amount of money
        return my_loot


s = Solution()
print(s.maxCoins([4, 4, 17, 7, 16, 16, 16, 15, 2, 3, 1, 17, 6, 12, 9]))
print(s.maxCoins(piles=[2, 4, 5]))
print(s.maxCoins(piles=[2, 4, 1, 2, 7, 8]))
print(s.maxCoins(piles=[9, 8, 7, 6, 5, 1, 2, 3, 4]))
