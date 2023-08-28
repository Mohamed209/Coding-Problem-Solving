# https://leetcode.com/problems/leaf-similar-trees
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaf_list):
            if not root.left and not root.right:
                leaf_list.append(root.val)
            if root.left:
                dfs(root.left, leaf_list)
            if root.right:
                dfs(root.right, leaf_list)

        leaves1, leaves2 = [], []
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1 == leaves2
