# Definition for a binary tree node.
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_sum_dict = {}
        q = collections.deque()
        q.append((root, 1))
        # level_sum_dict[1] = root.val
        while q:
            # length of curr level
            level_len = len(q)
            level_sum = 0
            # iterate through each level
            for _ in range(level_len):
                node, level = q.popleft()
                level_sum += node.val
                # add curr.left and curr.right to q if not empty
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            level_sum_dict[level] = level_sum
        print(level_sum_dict)
        # return result array
        return max(level_sum_dict, key=level_sum_dict.get)
