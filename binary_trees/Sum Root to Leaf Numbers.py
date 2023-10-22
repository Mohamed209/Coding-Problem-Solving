# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.res = 0

    def dfs(self, root, current_path):
        # one base case is when we rach leaf node
        # let us sum all elements across current path :)
        current_path.append(str(root.val))
        if not root.left and not root.right:
            print(current_path)
            self.res += int("".join(current_path))
            print(self.res)
            return
        if root.left:
            self.dfs(root.left, current_path)
            current_path.pop()
        if root.right:
            self.dfs(root.right, current_path)
            current_path.pop()

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, [])
        return self.res
