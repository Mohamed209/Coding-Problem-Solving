# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == 1:
            return max(cardPoints[0], cardPoints[-1])

        maximumScore = max(
            cardPoints[0] + self.maxScore(cardPoints[1:], k - 1),
            cardPoints[n - 1] + self.maxScore(cardPoints[: n - 1], k - 1),
        )
        return maximumScore
