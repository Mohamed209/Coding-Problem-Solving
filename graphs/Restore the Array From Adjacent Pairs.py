# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/description/
from collections import defaultdict
from typing import List


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        def dfs(graph: dict, start_node: int, path: dict):
            if start_node in path:
                return  # bypass closed loops
            path[start_node] = "visited"
            for neighbour in graph[start_node]:
                dfs(graph, neighbour, path)
            return path

        # represent adjacentPairs as graph
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        # print(graph)
        # we will have to start traversal from nodes at start or end of nums
        # those are elements which have only on neighbour and will make serialze the graph into list of adjacent neighbours
        start_node = None
        for node in graph:
            if len(graph[node]) == 1:
                start_node = node
                break
        path = dict()
        return list(dfs(graph, start_node, path).keys())


s = Solution()
print(s.restoreArray(adjacentPairs=[[4, -2], [1, 4], [-3, 1]]))
