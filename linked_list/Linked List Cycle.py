# https://leetcode.com/problems/linked-list-cycle
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        have_we_met_before = set()
        while head:
            if head in have_we_met_before:
                return True
            have_we_met_before.add(head)
            head = head.next
        return False
