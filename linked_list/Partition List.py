# https://leetcode.com/problems/partition-list/description
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        def connect_nodes(nodes_list: List[ListNode]):
            if len(nodes_list) == 0:
                return None
            for i in range(len(nodes_list) - 1):
                nodes_list[i].next = nodes_list[i + 1]

        if not head:
            return None
        nodes_less, nodes_larger_equal = [], []
        ptr = head
        while ptr:
            if ptr.val < x:
                nodes_less.append(ptr)
            else:
                nodes_larger_equal.append(ptr)
            ptr = ptr.next
        # handling some sneaky cases
        # if all lower or all larger than x
        if len(nodes_less) == 0:
            head = nodes_larger_equal[0]
            nodes_larger_equal[-1].next = None
            connect_nodes(nodes_larger_equal)
            return head
        if len(nodes_larger_equal) == 0:
            head = nodes_less[0]
            nodes_less[-1].next = None
            connect_nodes(nodes_less)
            return head
        # connect all nodes inside the two lists nodes_less, nodes_larger_equal
        connect_nodes(nodes_less)
        connect_nodes(nodes_larger_equal)
        # connect lists nodes_less, nodes_larger_equal to each other
        nodes_less[-1].next = nodes_larger_equal[0]
        # connect head to the first node in nodes_less
        head = nodes_less[0]
        # ground last node in nodes_larger_equal
        nodes_larger_equal[-1].next = None
        return head


head = ListNode(1)
head.next = ListNode(4)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(2)
s = Solution()
s.partition(head, 3)
