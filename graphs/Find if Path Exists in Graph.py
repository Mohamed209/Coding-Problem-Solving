# https://leetcode.com/problems/find-if-path-exists-in-graph/
from typing import List


class Solution:
    def validPath(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        def dfs(graph: dict, root: int, visited_path: set):
            if root not in visited_path:
                visited_path.add(root)
            for neighbour in graph[root]:
                if neighbour in visited_path:
                    continue
                if neighbour == destination:
                    return True
                if dfs(
                    graph, neighbour, visited_path
                ):  # if you find any valid path >> return True and exit
                    return True
            return False

        path = set()
        # convert edges to graph (node : neighbours ) pairs
        nodes = list(set([item for sublist in edges for item in sublist]))
        graph = {node: [] for node in nodes}
        if source == destination:
            return True
        if len(graph) == 0:
            return source == destination
        for p in edges:
            # bi-directional
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])
        return dfs(graph, source, path)


s = Solution()
print(
    s.validPath(
        n=10,
        edges=[
            [4, 3],
            [1, 4],
            [4, 8],
            [1, 7],
            [6, 4],
            [4, 2],
            [7, 4],
            [4, 0],
            [0, 9],
            [5, 4],
        ],
        source=5,
        destination=9,
    )
)
print(s.validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2))
print(
    s.validPath(
        n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5
    )
)
