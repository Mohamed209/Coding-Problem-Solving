# https://leetcode.com/problems/letter-case-permutation/
from typing import List


class Solution:
    @staticmethod
    def dfs(s, op, res):
        if len(s) == 0:
            if op not in res:
                res.append(op)
            return
        if s[0].isalpha():
            p0 = s[0]  # first possibility is to keep the char as it is
            p1 = s[0].swapcase()  # second possibility is to swap the char case
        else:
            p0, p1 = s[0], s[0]
        Solution.dfs(s[1:], op+p0, res)
        Solution.dfs(s[1:], op+p1, res)

    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        Solution.dfs(s, "", res)
        return res


# s = Solution()
# print(s.letterCasePermutation("a1b2"))
# print(s.letterCasePermutation("3z4"))
# print(s.letterCasePermutation(""))
