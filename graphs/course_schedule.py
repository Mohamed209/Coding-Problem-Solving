# https://leetcode.com/problems/course-schedule/
from typing import List


class Solution:
    @staticmethod
    def has_cycle(visited, node, preq_map):
        if node in visited:
            return True
        if preq_map[node] == []:
            return False
        visited.add(node)
        # dfs on all current node neighbours
        for neighbour in preq_map[node]:
            if Solution.has_cycle(node=neighbour, visited=visited, preq_map=preq_map):
                return True
        visited.remove(node)
        preq_map[node] = []
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # construct prerequisites map
        preq_map = {i: []for i in range(numCourses)}
        for preq in prerequisites:
            preq_map[preq[0]].extend(preq[1:])
        visited = set()
        for c in range(numCourses):
            if Solution.has_cycle(node=c, visited=visited, preq_map=preq_map):
                return False
        return True


s = Solution()
print(s.canFinish(6, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
