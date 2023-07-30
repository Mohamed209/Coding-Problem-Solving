# https://leetcode.com/problems/h-index
from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        def util(mid):
            cnt = 0
            for citation in citations:
                if citation >= mid:
                    cnt += 1
            return cnt

        left = 0
        right = len(citations)
        while left <= right:
            mid = (left + right) // 2
            res = util(mid)
            if res >= mid:
                left = mid + 1
            if res < mid:
                right = mid - 1
        return left - 1


s = Solution()
print(s.hIndex([0]))
print(s.hIndex(citations=[1, 1]))
print(s.hIndex(citations=[1000]))
print(s.hIndex(citations=[1, 3, 1]))
print(s.hIndex(citations=[9, 6, 7, 2, 1, 8]))
