# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
import collections
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        """
        the key is deal with the problem as graph pproblem not binary tree
        let us convert the binary tree to graph
        dfs the tree and for every node and add it as key in graph dict and corresponding values are [left,right,parent]
        """
        graph = collections.defaultdict(list)

        def build_graph(root: TreeNode, parent: Optional[TreeNode]):
            if root and parent:
                graph[root.val].append(parent.val)
                graph[parent.val].append(root.val)
            if root.left:
                build_graph(root=root.left, parent=root)
            if root.right:
                build_graph(root=root.right, parent=root)

        build_graph(root, None)
        """
        it is clear now that using this graph, distance k == level k in level order traversal
        """

        def bfs(
            graph: dict, start: int, level: int, target_level: int, visited: set
        ) -> List[int]:
            res = []
            queue = deque()
            print(graph)
            queue.appendleft((start, level))
            visited.add(start)
            while len(queue) > 0:
                start, level = queue.pop()
                print(start, "---", level)
                if level == target_level:
                    res.append(start)
                    continue
                if level > target_level:
                    break
                for neighbour in graph[start]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        queue.appendleft((neighbour, level + 1))
            return res

        visited = set()
        return bfs(graph, target.val, 0, k, visited)
