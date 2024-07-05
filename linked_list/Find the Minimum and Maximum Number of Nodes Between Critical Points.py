# https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/description/
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        next = head.next
        critical_points_idxs = []
        current_idx = (
            1  # from problem description nodes index labeled from 1 to len(list)
        )
        while next.next:
            # check local min or max
            if (next.val > curr.val and next.val > next.next.val) or (
                next.val < curr.val and next.val < next.next.val
            ):
                critical_points_idxs.append(current_idx)
            current_idx += 1
            # move pointers ahead
            curr = next
            next = next.next
        if len(critical_points_idxs) < 2:
            return [-1, -1]
        max_dist = critical_points_idxs[-1] - critical_points_idxs[0]
        min_dist = int(2e6)
        for i in range(len(critical_points_idxs) - 1):
            min_dist = min(
                min_dist, critical_points_idxs[i + 1] - critical_points_idxs[i]
            )
        return [min_dist, max_dist]
