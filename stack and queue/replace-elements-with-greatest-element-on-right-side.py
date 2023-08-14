# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []
        for i in range(len(arr), 0, -1):
            if len(res) == 0:
                res.append(-1)
                continue
            if arr[i] > res[-1]:
                res.append(arr[i])
            else:
                res.append(res[-1])
        return res[::-1]
