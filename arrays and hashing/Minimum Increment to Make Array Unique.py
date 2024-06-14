# https://leetcode.com/problems/minimum-increment-to-make-array-unique/?envType=daily-question&envId=2024-06-14
from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        freq = {k: 0 for k in range(max(nums) + len(nums))}
        for num in nums:
            freq[num] += 1
        for k in freq:
            if freq[k] > 1:
                freq[k + 1] += freq[k] - 1
                res += freq[k] - 1
        return res


s = Solution()
s.minIncrementForUnique([3, 2, 1, 2, 1, 7])
s.minIncrementForUnique([1, 2, 3])
