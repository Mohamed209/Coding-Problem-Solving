# https://leetcode.com/problems/koko-eating-bananas
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k must be in range(1,len(piles))
        # since this range is already sorted , we can use binary search to find min k
        left = 1
        right = max(piles)
        while left < right:
            mid = (right + left) // 2
            # now let koko eats with rate mid bananas , how many hours she needs to finish ?
            hours = sum([ceil(p / mid) for p in piles])
            """
            we have two options here
            1- if koko finish in hours > h , this means that she will need to speed up eating more to fit in h hours
            so in this case we search in the right subarray
            2- if koko finish in hours < h , this means she eats little bit very fast , although we still fit in h hours,
            we need to minimimize k so we continue search in left subarray
            """
            if hours <= h:
                right = mid
            else:
                left = mid + 1
        return left
