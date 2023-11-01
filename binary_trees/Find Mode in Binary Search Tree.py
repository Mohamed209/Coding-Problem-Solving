# https://leetcode.com/problems/find-mode-in-binary-search-tree/description
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(root: Optional[TreeNode], visited: dict):
            if root.val not in visited:
                visited[root.val] = 1
            else:
                visited[root.val] += 1
            if root.left:
                dfs(root.left, visited)
            if root.right:
                dfs(root.right, visited)

        visited = {}
        dfs(root, visited)
        mode = max(visited.values())
        return [k for k, v in visited.items() if v == mode]
