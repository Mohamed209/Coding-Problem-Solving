# https://leetcode.com/problems/palindrome-linked-list/description/?envType=daily-question&envId=2024-03-22
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def get_middle(head):
            """
            find middle element of linkedlist
            """
            slow, fast = head, head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow

        def reverse(head):
            if not head:
                return None
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        reverse_head = reverse(get_middle(head))
        temp1 = head
        temp2 = reverse_head
        while temp2:
            if temp1.val != temp2.val:
                return False
            temp1 = temp1.next
            temp2 = temp2.next
        return True
