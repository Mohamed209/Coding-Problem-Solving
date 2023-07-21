# https://leetcode.com/problems/combination-sum-iii/

# brute forch first iteration
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def dfs(start: int, path: List[int]):
            if len(path) == k and sum(path) != n:
                return
            if len(path) == k and sum(path) == n:
                sp = sorted(path)
                if sp not in res:
                    res.append((sp.copy()))
                return
            for i in range(1, 10):
                if i < n and i not in path:
                    path.append(i)
                    # visited.add(start)
                    dfs(start=i, path=path)
                    path.pop()

        res = []
        visited = set()
        for start in range(1, 10):
            # start dfs from every number in range(1,10)
            # inital path = [start]
            dfs(start, [start])
            visited.clear()
        return res


s = Solution()
print(s.combinationSum3(k=3, n=15))
