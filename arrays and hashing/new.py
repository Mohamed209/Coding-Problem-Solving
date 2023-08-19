# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        visited_cases = {}
        richest_kid = max(candies)
        res = []
        for kid in candies:
            if kid not in visited_cases:
                if kid == richest_kid:
                    visited_cases[kid] = True
                else:
                    visited_cases[kid] = kid + extraCandies >= richest_kid
            res.append(visited_cases[kid])
        return res


s = Solution()
print(s.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
