from typing import List, Optional
from collections import deque
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []
        q: deque = deque([])
        q.append(root)
        while q:
            root_node = q.popleft()
            res.append(root_node.val)
            if root_node.left:
                q.append(root_node.left)
            if root_node.right:
                q.append(root_node.right)
        return res


s = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(s.levelOrder(root))
