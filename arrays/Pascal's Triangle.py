# https://leetcode.com/problems/pascals-triangle/
from typing import List


def pascal(x: List[int]) -> List[int]:
    res = [1]
    for i in range(len(x)-1):
        res.append(x[i]+x[i+1])
    res.append(1)
    return res


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for row in range(numRows-1):
            result.append(pascal(result[-1]))
        return result
