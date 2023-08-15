# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/
from typing import List


class Solution:
    def arraySign(self, nums: List[int]) -> int:
        neg_cnt = 0
        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                neg_cnt += 1
        if neg_cnt % 2 == 0:
            return 1
        else:
            return -1
