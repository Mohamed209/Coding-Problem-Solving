# https://leetcode.com/problems/diagonal-traverse-ii/description
from collections import deque
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        queue = deque([(0, 0)])
        ans = []
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            # add two neighbours for every cell
            if row < len(nums) - 1 and col == 0:
                queue.append((row + 1, col))
            if col < len(nums[row]) - 1:
                queue.append((row, col + 1))
        return ans


s = Solution()
print(
    s.findDiagonalOrder(
        nums=[[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
    )
)
print(s.findDiagonalOrder(nums=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
