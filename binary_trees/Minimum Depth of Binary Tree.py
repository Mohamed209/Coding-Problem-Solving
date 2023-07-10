# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(root: TreeNode, level: int):
            queue = deque()
            queue.appendleft((root, level))
            while len(queue) > 0:
                current_node = queue.pop()
                print(current_node[0].val, level)
                """
                simply start bfs traversal , once you land any leaf node at any level
                immediately retrun this level
                """
                if not current_node[0].left and not current_node[0].right:
                    return current_node[1]
                if current_node[0].left:
                    queue.appendleft((current_node[0].left, current_node[1] + 1))
                if current_node[0].right:
                    queue.appendleft((current_node[0].right, current_node[1] + 1))

        if not root:
            return 0
        return bfs(root=root, level=1)
