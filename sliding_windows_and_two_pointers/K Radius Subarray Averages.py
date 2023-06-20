# https://leetcode.com/problems/k-radius-subarray-averages/
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # Initially all equal -1
        averages = [-1] * n
        # Sliding sum initialization
        window = sum(nums[: 2 * k])
        for i in range(k, n - k):
            window += nums[i + k]
            averages[i] = window // (2 * k + 1)
            window -= nums[i - k]
        return averages


s = Solution()
print(s.getAverages(nums=[7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
