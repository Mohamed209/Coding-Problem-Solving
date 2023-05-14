# https://leetcode.com/problems/rotate-image/
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def swap(matrix, visited, r1, c1, r2, c2):
            # swap two elements in matrix given their coords r,c
            if (r1, c1) in visited:
                return
            tmp = matrix[r1][c1]
            matrix[r1][c1] = matrix[r2][c2]
            matrix[r2][c2] = tmp
            visited.add((r1, c1))
            visited.add((r2, c2))

        # the 90 degree clockwise rotation is transpose in reversed order
        # 1- tranpose the matrix ===> O(rows*cols)
        ROWS = len(matrix)
        COLS = len(matrix[0])
        visited = set()
        for r in range(ROWS):
            for c in range(COLS):
                swap(matrix, visited, r, c, c, r)
        # 2- reverse the columns order of the swapped image ===> O(rows*cols)
        for idx, row in enumerate(matrix):
            matrix[idx] = row[::-1]


s = Solution()
s.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s.rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
