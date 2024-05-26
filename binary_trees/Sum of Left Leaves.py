from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(root):
            nonlocal ans
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                ans += root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ans


s = Solution()
root = TreeNode(
    val=1,
    left=TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5)),
    right=TreeNode(val=3),
)
s.sumOfLeftLeaves(root)
