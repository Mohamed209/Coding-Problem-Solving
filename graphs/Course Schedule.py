# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    def dfs(self, graph: dict, start: int, visited: set) -> bool:
        if start in visited:
            return False
        if graph[start] == "x":  # graph dfs pruning
            return True
        visited.add(start)
        for neighbour in graph[start]:
            if not self.dfs(graph=graph, start=neighbour, visited=visited):
                return False
        visited.remove(start)
        graph[start] = "x"
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if prerequisites == []:
            return True
        # convert prerequisites to graph (node : neighbours ) pairs
        nodes = list(set([item for sublist in prerequisites for item in sublist]))
        graph = {node: [] for node in nodes}
        visited = set()
        for p in prerequisites:
            graph[p[0]].append(p[1])
        # check every node to handle isolated clusters
        for k in graph.keys():
            if not self.dfs(graph, k, visited):
                return False
        return True


s = Solution()
print(s.canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
print(s.canFinish(2, [[1, 0]]))
print(s.canFinish(2, [[1, 0], [0, 1]]))
print(s.canFinish(1, []))
print(
    s.canFinish(
        20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
    )
)
