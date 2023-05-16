# https://leetcode.com/problems/set-matrix-zeroes/
# TODO : introduce speed up
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeros_locations = set()
        rows = len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros_locations.add((r, c))
        print(zeros_locations)
        affected_rows = set([x[0] for x in zeros_locations])
        affected_cols = set(x[1] for x in zeros_locations)
        for row in affected_rows:
            matrix[row] = [0] * cols
        for col in affected_cols:
            for row in range(rows):
                matrix[row][col] = 0
        return


s = Solution()
s.setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
