# https://leetcode.com/problems/subsets/
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            for ex in res[1:]:
                res.append(ex+[num])
            res.append([num])
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
