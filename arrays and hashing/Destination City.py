# https://leetcode.com/problems/destination-city
from typing import List
import itertools


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        all_cities = set(list(itertools.chain(*paths)))
        for citya, cityb in paths:
            all_cities.remove(citya)
        return all_cities.pop()


s = Solution()
s.destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
