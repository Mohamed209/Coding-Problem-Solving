# https://leetcode.com/problems/sort-list
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l.sort()
        for i in range(len(l)):
            l[i] = ListNode(val=l[i])
        for i in range(len(l) - 1):
            l[i].next = l[i + 1]
        return l[0]
