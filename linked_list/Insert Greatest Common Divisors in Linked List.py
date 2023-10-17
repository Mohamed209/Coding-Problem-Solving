# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/
from math import gcd
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        original_pointer = head
        while head and head.next:
            new_node = ListNode(val=gcd(head.val, head.next.val), next=head.next)
            head.next = new_node
            head = head.next.next
        return original_pointer
