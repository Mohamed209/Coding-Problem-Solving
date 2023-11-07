# https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
import math
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrival_time = []
        for mon_dist, mon_speed in zip(dist, speed):
            arrival_time.append(math.ceil(mon_dist / mon_speed))
        arrival_time.sort()
        score = 0
        for i in range(len(arrival_time)):
            if (
                arrival_time[i] <= i
            ):  # one monster arrival time is before I can reload the weapon
                return score
            score += 1
        return len(arrival_time)  # killed them all


s = Solution()
s.eliminateMaximum(dist=[3, 2, 4], speed=[5, 3, 2])
s.eliminateMaximum(dist=[4, 3, 4], speed=[1, 1, 2])
