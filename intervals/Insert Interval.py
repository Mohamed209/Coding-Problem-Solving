# https://leetcode.com/problems/insert-interval/
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        res = []
        for interval in intervals:
            if newInterval[0] > interval[1] or newInterval[1] < interval[0]:
                # here we are 100% sure there is no overlap between new interval and current interval
                res.append(interval)
            else:
                # new interval has overlap with current interval --> merge them together
                merged = [
                    min(newInterval[0], interval[0]),
                    max(newInterval[1], interval[1]),
                ]
                newInterval = merged.copy()
        # insert new interval with result
        if len(res) == 0:
            res.append(newInterval)
            return res
        return sorted(res + [newInterval], key=lambda x: x[0])


s = Solution()
print(s.insert([[2, 6], [7, 9]], [15, 18]))
print(s.insert([[2, 5], [6, 7], [8, 9]], [0, 1]))
print(s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]))
print(
    s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
)
print(s.insert(intervals=[[1, 5]], newInterval=[2, 3]))
print(s.insert([[1, 5]], [6, 8]))
print(s.insert([[0, 2], [3, 9]], [6, 8]))
