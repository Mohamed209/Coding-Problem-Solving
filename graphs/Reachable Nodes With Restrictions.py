# https://leetcode.com/problems/reachable-nodes-with-restrictions/
from typing import List


class Solution:
    def reachableNodes(
        self, n: int, edges: List[List[int]], restricted: List[int]
    ) -> int:
        # convert edges to graph (node : neighbours) pairs
        nodes = list(set([item for sublist in edges for item in sublist]))
        graph = {node: [] for node in nodes}
        for e in edges:
            # bi-directional
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def dfs(root: int, path: set, graph: dict, restricted: set):
            if root in path or root in restricted:
                # stop graph dfs if we land visited or restricted node
                return 0
            path.add(root)
            for neighbour in graph[root]:
                dfs(neighbour, path, graph, restricted)
            return len(path)

        path = set()  # this should save longest dfs traversal path from root node
        restricted_hash_set = set(restricted)  # hashset for O(1) queries
        return dfs(
            0, path, graph, restricted_hash_set
        )  # start dfs from node 0 and keep update dfs path for with every valid node


s = Solution()
print(
    s.reachableNodes(
        n=7, edges=[[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]], restricted=[4, 5]
    )
)
