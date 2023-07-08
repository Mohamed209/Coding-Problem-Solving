# https://leetcode.com/problems/detonate-the-maximum-bombs/
import math
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def check_intersections(
            x0: int, y0: int, r0: int, x1: int, y1: int, r1: int
        ) -> bool:
            # circle 1: (x0, y0), radius r0
            # circle 2: (x1, y1), radius r1
            d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
            return r0 >= d  # r0 will detonate r1

        def dfs(graph: dict, root: int, visited: set) -> int:
            if root in visited:
                return
            visited.add(root)
            for neighbour in graph[root]:
                dfs(graph, neighbour, visited)
            return len(visited)

        # construct graph representation from bombs list of list input
        graph = {}
        for i in range(len(bombs)):
            graph[i] = []
            for j in range(len(bombs)):
                if i != j:
                    if check_intersections(
                        bombs[i][0],
                        bombs[i][1],
                        bombs[i][2],
                        bombs[j][0],
                        bombs[j][1],
                        bombs[j][2],
                    ):
                        graph[i].append(j)
        path = set()
        mass_distruction = 1
        for bomb in graph:
            mass_distruction = max(mass_distruction, dfs(graph, bomb, path))
            path.clear()
        return mass_distruction


s = Solution()
s.maximumDetonation(bombs=[[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]])
s.maximumDetonation(bombs=[[1, 1, 5], [10, 10, 5]])
s.maximumDetonation(bombs=[[2, 1, 3], [6, 1, 4]])
