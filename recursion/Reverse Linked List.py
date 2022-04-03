# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case
        if head == None:
            return head
        tmp = head
        if head.next:
            tmp = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return tmp
