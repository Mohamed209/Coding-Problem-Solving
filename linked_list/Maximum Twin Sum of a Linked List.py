# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    naive ---> TLE
    """

    # def pairSum(self, head: Optional[ListNode]) -> int:
    #     iterator = head
    #     size = 0
    #     max_twin_sum = 0
    #     while iterator:
    #         size += 1
    #         iterator = iterator.next
    #     left = head  # slow pointer
    #     right = head  # fast pointer
    #     left_idx = 0
    #     right_idx = 0
    #     while left_idx < size // 2:
    #         # move right pointer
    #         while right_idx < size - 1 - left_idx:
    #             right = right.next
    #             right_idx += 1
    #         max_twin_sum = max(max_twin_sum, left.val + right.val)
    #         left_idx += 1
    #         left = left.next
    #         right = left
    #         right_idx = left_idx
    #     return max_twin_sum
    """
    using extra O(N) space 
    """

    def pairSum(self, head: Optional[ListNode]) -> int:
        # convert linkedlist to arraylist , it works well , but there is no fun in that :)
        vals = []
        max_twin_sum = 0
        while head:
            vals.append(head.val)
            head = head.next
        left = 0
        right = len(vals) - 1
        while left < len(vals) // 2:
            max_twin_sum = max(max_twin_sum, vals[left] + vals[right])
            left += 1
            right -= 1
        return max_twin_sum
