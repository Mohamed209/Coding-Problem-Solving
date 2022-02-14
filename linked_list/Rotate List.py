# problem : https://leetcode.com/problems/rotate-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        # first we need to find the length of the linked list
        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        #============================#
        k = k % length
        if k == 0:
            return head
        # travel to length-k-1
        i = 0
        cur = head
        while(i < length-k-1):
            i += 1
            cur = cur.next
        newhead = cur.next
        cur.next = None
        tail.next = head
        return newhead
