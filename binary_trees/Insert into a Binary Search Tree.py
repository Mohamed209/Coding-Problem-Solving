# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # what if root is none:
        if not root:
            return TreeNode(val)
        # base case is to reach leaf node
        if not root.left and not root.right:
            if val > root.val:
                root.right = TreeNode(val)
            else:
                root.left = TreeNode(val)
            return root
        if val > root.val:
            # travel to the right subtree
            root.right = self.insertIntoBST(root.right, val)
        else:
            # travel to the left subtree
            root.left = self.insertIntoBST(root.left, val)
        return root
