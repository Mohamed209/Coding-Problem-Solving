# https://leetcode.com/problems/reshape-the-matrix/
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)  # original rows
        m = len(mat[0])  # original cols
        if r*c != m*n:  # r*c must equal m*n do perform the reshaping
            return mat
        else:
            k = 0
            v = 0
            ans=[]
            for i in range(r):
                ans.append([])
                for j in range(c):
                    ans[i].append(0)
            for i in range(n):
                for j in range(m):
                    ans[k][v] = mat[i][j]
                    v += 1
                    if v == c:
                        v = 0
                        k += 1
        return ans