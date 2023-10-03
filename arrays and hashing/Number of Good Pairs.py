# https://leetcode.com/problems/number-of-good-pairs/description
from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq_map = Counter(nums)  # create frequency table for every num in nums
        no_of_good_pairs = 0
        # if a number is found n times in the array - where n>1 - then number of pairs can be constructed from this number is (n*(n-1))//2
        for num in freq_map:
            n = freq_map[num]
            if n > 1:
                no_of_good_pairs += (n * (n - 1)) // 2
        return no_of_good_pairs
