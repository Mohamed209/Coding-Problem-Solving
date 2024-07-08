# https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
from sortedcontainers import SortedList


class Solution(object):
    def findTheWinner(self, n, k):
        cycle = SortedList(range(1, n + 1)) # to perform O(log(n)) deletion
        index = 0
        while len(cycle) > 1:
            index = (index + k - 1) % len(cycle)
            cycle.pop(index)
        return cycle[0]
