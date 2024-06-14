# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/?envType=daily-question&envId=2024-06-14
from typing import List


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # each student must be moved to the nearest seat
        seats.sort()
        students.sort()
        res = 0
        for stdpos, seatpos in zip(students, seats):
            res += abs(stdpos - seatpos)
        return res


s = Solution()
print(s.minMovesToSeat(seats=[3, 1, 5], students=[2, 7, 4]))
print(s.minMovesToSeat(seats=[4, 1, 5, 9], students=[1, 3, 2, 6]))
print(s.minMovesToSeat(seats=[2, 2, 6, 6], students=[1, 3, 2, 6]))
