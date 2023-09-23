# https://leetcode.com/problems/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                ans += 1
                prevEnd = min(end, prevEnd)
        return ans
