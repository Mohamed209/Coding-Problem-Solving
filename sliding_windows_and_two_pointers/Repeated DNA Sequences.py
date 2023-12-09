# https://leetcode.com/problems/repeated-dna-sequences
from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen_before, res = set(), set()
        for i in range(len(s) - 9):
            current_window = s[i : i + 10]
            if current_window in seen_before:
                res.add(current_window)
            else:
                seen_before.add(current_window)
        return list(res)


s = Solution()
s.findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
