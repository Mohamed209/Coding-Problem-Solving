# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/
from typing import Optional


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head.next:
            return head
        # 1- need to know the length of the linkedlist
        iterator = head
        length = 0
        while iterator:
            length += 1
            iterator = iterator.next
        # 2- land at nodes at k position from start and from end
        left_node = head
        left_index = 1
        right_node = head
        right_index = 1
        while left_index < k:
            left_index += 1
            left_node = left_node.next
        while right_index < length - k + 1:
            right_index += 1
            right_node = right_node.next
        # 3- swap left and right nodes
        tmp = left_node.val
        left_node.val = right_node.val
        right_node.val = tmp
        return head
