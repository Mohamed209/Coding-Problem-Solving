# https://leetcode.com/problems/maximum-number-of-balloons/
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # ref = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        freq = Counter(text)
        max_ballons = 0
        # notice ref dict , every time we are able to construct ballon , we reduce the count of every key in freq by its reference value
        while (
            freq["b"] >= 1
            and freq["a"] >= 1
            and freq["l"] >= 2
            and freq["o"] >= 2
            and freq["n"] >= 1
        ):
            max_ballons += 1
            freq["b"] -= 1
            freq["a"] -= 1
            freq["l"] -= 2
            freq["o"] -= 2
            freq["n"] -= 1

        return max_ballons


s = Solution()
print(s.maxNumberOfBalloons(text="loonbalxballpoon"))
