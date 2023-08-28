# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        lst = [root.val]
        res = 0

        def dfs(root):
            nonlocal res
            if root == None:
                return
            if root.val >= max(lst):
                res += 1
            lst.append(root.val)
            dfs(root.left)
            dfs(root.right)
            lst.pop()

        dfs(root)
        return res
