# https://leetcode.com/problems/spiral-matrix/description/
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        rows, cols = len(matrix), len(matrix[0])

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited:
                return
            visited.add((r, c))
            res.append(matrix[r][c])
            if r <= c + 1:
                dfs(r, c + 1)  # →
            dfs(r + 1, c)  # ↓
            dfs(r, c - 1)  # ←
            dfs(r - 1, c)  # ↑ going up till we row >= col

        dfs(0, 0)
        return res


s = Solution()
s.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
