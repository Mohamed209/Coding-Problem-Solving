# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        l1ptr, l2ptr = l1, l2
        l1list, l2list = [], []
        while l1ptr:
            l1list.append(l1ptr.val)
            l1ptr = l1ptr.next
        while l2ptr:
            l2list.append(l2ptr.val)
            l2ptr = l2ptr.next
        l1num = int("".join([str(c) for c in reversed(l1list)]))
        l2num = int("".join([str(c) for c in reversed(l2list)]))
        lsum = list(reversed(str(l1num + l2num)))
        root = ListNode(val=int(lsum[0]))
        ptr = root
        for i in range(1, len(lsum)):
            ptr.next = ListNode(val=int(lsum[i]))
            ptr = ptr.next
        return root
