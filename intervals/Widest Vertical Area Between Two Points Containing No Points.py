# https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points
from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()
        max_width = 0
        for i in range(len(points) - 1):
            max_width = max(points[i + 1][0] - points[i][0], max_width)
        return max_width


if __name__ == "__main__":
    s = Solution()
    print(s.maxWidthOfVerticalArea([[8, 7], [9, 9], [7, 4], [9, 7]]))
    print(s.maxWidthOfVerticalArea([[3, 1], [9, 0], [1, 0], [1, 4], [5, 3], [8, 8]]))