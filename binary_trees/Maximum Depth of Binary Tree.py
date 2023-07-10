# problem : https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/535/
# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root: TreeNode, level: int, deepest_level: int):
            queue = deque()
            queue.appendleft((root, level))
            while len(queue) > 0:
                current_node = queue.pop()
                print(current_node[0].val, level)
                """
                simply start bfs traversal , until you visit the farthest level from root node
                """
                deepest_level = current_node[1]
                if current_node[0].left:
                    queue.appendleft((current_node[0].left, current_node[1] + 1))
                if current_node[0].right:
                    queue.appendleft((current_node[0].right, current_node[1] + 1))
            return deepest_level

        if not root:
            return 0
        return bfs(root=root, level=1, deepest_level=1)
