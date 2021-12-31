# problem : https://leetcode.com/problems/path-sum/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        targetSum -= root.val
        if ((targetSum == 0) and (not root.left) and (not root.right)):
            return True
        if self.hasPathSum(root.left, targetSum):
            return True
        elif self.hasPathSum(root.right, targetSum):
            return True
        else:
            return False
