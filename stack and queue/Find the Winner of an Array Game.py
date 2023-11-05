# https://leetcode.com/problems/find-the-winner-of-an-array-game/description/
from typing import List
from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k >= len(arr):
            return max(arr)
        arrq = deque([[item, 0] for item in arr])  # queue of (item,wins_streak) pairs
        while True:
            first, second = arrq.popleft(), arrq.popleft()  # O(1)
            if first[0] > second[0]:
                winner = first
                loser = second
            else:
                winner = second
                loser = first
            winner[-1] += 1  # increment win streak for current winner
            if winner[-1] == k:
                return winner[0]
            # next round
            arrq.appendleft(winner)  # O(1)
            arrq.append(loser)  # O(1)


s = Solution()
s.getWinner(arr=[2, 1, 3, 5, 4, 6, 7], k=2)
