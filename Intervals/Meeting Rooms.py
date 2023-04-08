# https://www.lintcode.com/problem/920/
from typing import List


# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        for i in range(1, len(intervals)):
            if intervals[i - 1].end > intervals[i].start:
                return False
        return True


s = Solution()
print(s.can_attend_meetings([Interval(0, 30), Interval(15, 20), Interval(5, 10)]))
print(s.can_attend_meetings([Interval(5, 8), Interval(9, 15)]))
