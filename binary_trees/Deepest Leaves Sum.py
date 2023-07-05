# https://leetcode.com/problems/deepest-leaves-sum/description/
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append((root, 0))  # node,level
        deepest_level = 0
        res = 0
        while q:
            node, level = q.pop()
            if level == deepest_level:
                res += node.val
            if level > deepest_level:
                # entered new level
                res = node.val
                deepest_level = level
            if node.left:
                q.appendleft((node.left, level + 1))
            if node.right:
                q.appendleft((node.right, level + 1))
        return res
