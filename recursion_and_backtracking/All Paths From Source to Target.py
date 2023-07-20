# https://leetcode.com/problems/all-paths-from-source-to-target/
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(graph: List[List[int]], root: int, path: List[int]):
            # base case to stop recursion
            if root == len(graph) - 1:
                res.append(path.copy())
                return
            for neigbour in graph[root]:
                path.append(neigbour)
                dfs(graph, neigbour, path)
                path.pop()

        res = []
        dfs(graph, 0, path=[0])
        return res


s = Solution()
print(s.allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))
