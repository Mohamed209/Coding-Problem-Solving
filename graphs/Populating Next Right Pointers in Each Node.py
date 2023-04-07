# problem : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self,
        val: int = 0,
        left: "Node" = None,
        right: "Node" = None,
        next: "Node" = None,
    ):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        queue = deque()
        queue.appendleft(root)
        while queue:
            currnode = queue.pop()
            if currnode and currnode.left and currnode.right:
                currnode.left.next = currnode.right
                if currnode.next:
                    currnode.right.next = currnode.next.left
                queue.appendleft(currnode.left)
                queue.appendleft(currnode.right)
        return root
