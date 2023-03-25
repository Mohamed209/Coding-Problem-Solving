# problem : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# Definition for a Node.
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    @staticmethod
    def populatelowerlevel(node):
        current = node
        while current:
            current.left.next = current.right
            if current.next:
                current.right.next = current.next.left
            current = current.next

    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftnode = root
        while (leftnode and leftnode.left):
            Solution.populatelowerlevel(leftnode)
            leftnode = leftnode.left
        return root
