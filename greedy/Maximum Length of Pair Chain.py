from typing import List

# https://leetcode.com/problems/maximum-length-of-pair-chain/


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key=lambda x: x[1])
        chain = [pairs[0]]
        for p in pairs[1:]:
            if p[0] > chain[-1][1]:
                chain.append(p)
        return len(chain)


s = Solution()
print(s.findLongestChain(pairs=[[1, 2], [7, 8], [4, 5]]))
