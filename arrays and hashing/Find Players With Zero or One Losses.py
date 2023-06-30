# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners_dict = Counter([match[0] for match in matches])
        losers_dict = Counter([match[1] for match in matches])
        alltime_winners = []
        only_1match_losers = []
        for key in winners_dict:
            if key not in losers_dict:
                alltime_winners.append(key)
        for key in losers_dict:
            if losers_dict[key] == 1:
                only_1match_losers.append(key)
        alltime_winners.sort()
        only_1match_losers.sort()
        return alltime_winners, only_1match_losers


s = Solution()
print(
    s.findWinners(
        matches=[
            [1, 3],
            [2, 3],
            [3, 6],
            [5, 6],
            [5, 7],
            [4, 5],
            [4, 8],
            [4, 9],
            [10, 4],
            [10, 9],
        ]
    )
)
