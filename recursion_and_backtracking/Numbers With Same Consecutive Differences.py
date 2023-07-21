# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def dfs(start: int, path: List[int]):
            if len(path) == n:
                # if we made it to this stage , this means we can construct the integer
                # respecting the rule that difference between every two consecutive digits is k
                res.append(int("".join([str(c) for c in path.copy()])))
                return
            # continue dfs for all current start neighbours
            # every start has 9 neighbours from 0 to 9
            for i in range(0, 10):
                if abs(start - i) == k:
                    # we shall only continue the dfs if this path seems promising :)
                    path.append(i)
                    dfs(i, path)
                    path.pop()

        res = []
        for start in range(1, 10):
            # start dfs from every number in range(1,10)
            # inital path = [start]
            dfs(start, [start])
        return res


s = Solution()
print(s.numsSameConsecDiff(3, 7))
