# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(
        self, headA: ListNode, headB: ListNode
    ) -> Optional[ListNode]:
        visited = set()
        # traverse A
        ptra = headA
        while ptra:
            visited.add(ptra)
            ptra = ptra.next
        ptrb = headB
        while ptrb:
            if ptrb in visited:
                return ptrb
            ptrb = ptrb.next
        return None
