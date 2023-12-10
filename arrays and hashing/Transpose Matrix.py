# https://leetcode.com/problems/transpose-matrix/description
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])
        res = []
        for col in range(cols):
            res_row = []
            for row in range(rows):
                res_row.append(matrix[row][col])
            res.append(res_row)
        return res


s = Solution()
s.transpose(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
