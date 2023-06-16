# https://leetcode.com/problems/search-a-2d-matrix-ii/description/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        lastr = rows
        for r in range(rows):
            if matrix[r][0] == target:
                return True
            elif matrix[r][0] > target:
                lastr = r
                break  # reduce search space
        # the number must be in rows [0 : lastr]
        for r in range(0, lastr):
            for c in range(cols):
                if matrix[r][c] == target:
                    return True
                elif matrix[r][c] > target:
                    break  # reduce search space
        return False


s = Solution()
print(s.searchMatrix([[1, 4], [2, 5]], 5))
