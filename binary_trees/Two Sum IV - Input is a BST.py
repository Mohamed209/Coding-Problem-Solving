from collections import deque
from typing import Optional
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        queue = deque()
        queue.append(root)
        available = set()
        while len(queue) > 0:
            popped = queue.popleft()
            if k-popped.val in available:
                return True
            else:
                available.add(popped.val)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        return False
