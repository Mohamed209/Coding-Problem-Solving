# https://leetcode.com/problems/coin-change-ii/
from typing import List

# TLE

class Solution:
    @staticmethod
    def dfs(money: int, coins: List[int], res: set, currpath: List[int]):
        """
        depth first traversal for the decesion tree of the problem
        """
        if money == 0:
            # I found a way to construct money from coins
            return True
        elif money < 0:
            # bace case but dead end
            return False
        for coin in coins:
            currpath.append(coin)
            if Solution.dfs(money - coin, coins, res, currpath):
                curpathsorted = tuple(sorted(currpath.copy()))
                if curpathsorted not in res:
                    res.add(curpathsorted)
            currpath.pop()

    def change(self, amount: int, coins: List[int]) -> int:
        res = set()
        path = []
        Solution.dfs(amount, coins, res, path)
        print(res)
        return len(res)


s = Solution()
print(s.change(5, [1, 2, 5]))
print(s.change(10, [2, 5, 3, 6]))
print(s.change(3, [2]))
