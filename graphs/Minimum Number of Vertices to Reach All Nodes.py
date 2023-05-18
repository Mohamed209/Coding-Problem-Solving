# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/
from typing import List


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        We only have to count the number of nodes with zero incoming edges.
        """
        result = []
        nodes_with_edges = set([edge[0] for edge in edges])
        neighbours = set(edge[1] for edge in edges)
        for node in nodes_with_edges:
            if node not in neighbours:
                result.append(node)
        return result


s = Solution()
print(s.findSmallestSetOfVertices(n=6, edges=[[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]))
print(s.findSmallestSetOfVertices(n=5, edges=[[0, 1], [2, 1], [3, 1], [1, 4], [2, 4]]))
