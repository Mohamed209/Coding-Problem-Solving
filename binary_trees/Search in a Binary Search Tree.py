# problem https://leetcode.com/problems/search-in-a-binary-search-tree/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val == val:
            return root
        if val < root.val:
            # search in the left subtree
            return self.searchBST(root.left, val)
        elif val > root.val:
            # search in the right subtree
            return self.searchBST(root.right, val)
