# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # at first we need to find the length of the list
        curr = head
        nodes_count = 0
        while curr:
            nodes_count += 1
            curr = curr.next
        if nodes_count == 1:
            return None
        elif nodes_count == n:
            head = head.next
            return head
        # second loop until nodes_count-n-1
        curr2 = head
        for _ in range(nodes_count-n-1):
            curr2 = curr2.next
        curr2.next = curr2.next.next
        return head
