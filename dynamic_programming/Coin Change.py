# https://leetcode.com/problems/coin-change/
from typing import List
import math


class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def dfs(self, coins, amount):
        if amount in self.cache:
            return self.cache[amount]
        if amount == 0:
            # base case , reached valid path
            return 0
        elif amount < 0:
            # base case , dead end
            return math.inf
        res = min([1+self.dfs(coins, amount-coin) for coin in coins])
        self.cache[amount] = res
        return res

    def coinChange(self, coins: List[int], amount: int) -> int:
        shortest_path = self.dfs(coins, amount)
        if shortest_path == math.inf:
            return -1
        return shortest_path


s = Solution()
print(s.coinChange([1, 2, 5], 11))
