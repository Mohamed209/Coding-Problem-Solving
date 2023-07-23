# https://leetcode.com/problems/minimum-falling-path-sum/
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def dfs(row: int, col: int, cache: dict):
            if (row, col) in cache:
                return cache[(row, col)]
            if col < 0 or col >= len(matrix[0]):
                return int(1e4)
            if row == len(matrix):
                return 0
            print(row, col)
            cache[(row, col)] = matrix[row][col] + min(
                dfs(row + 1, col - 1, cache),
                dfs(row + 1, col, cache),
                dfs(row + 1, col + 1, cache),
            )
            return cache[(row, col)]

        res = int(1e9)
        cache = {}
        for col in range(len(matrix[0])):
            res = min(res, dfs(0, col, cache))
        return res


s = Solution()
print(
    s.minFallingPathSum(
        matrix=[
            [100, -42, -46, -41],
            [31, 97, 10, -10],
            [-58, -51, 82, 89],
            [51, 81, 69, -51],
        ]
    )
)
