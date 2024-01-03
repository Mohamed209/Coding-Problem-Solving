# https://leetcode.com/problems/number-of-laser-beams-in-a-bank
from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        lasers = []
        for row in bank:
            laser_cnt = row.count("1")
            if laser_cnt > 0:
                lasers.append(laser_cnt)
        print(lasers)
        total = 0
        for i in range(len(lasers) - 1):
            total += lasers[i] * lasers[i + 1]
        return total


s = Solution()
print(s.numberOfBeams(bank=["011001", "000000", "010100", "001000"]))
