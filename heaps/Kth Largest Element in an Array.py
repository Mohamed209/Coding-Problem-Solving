import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-i for i in nums]
        heapq.heapify(nums)
        for _ in range(k):
            res = heapq.heappop(nums)
        return res * -1


s = Solution()
print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
