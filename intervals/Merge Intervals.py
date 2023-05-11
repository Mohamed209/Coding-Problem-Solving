# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key=lambda x: x[0])
        result = [intervals[0]]

        def there_is_overlap(intervalx: List[int], intervaly: List[int]) -> bool:
            if intervalx[0] > intervaly[1] or intervalx[1] < intervaly[0]:
                return False
            else:
                return True

        for interval in intervals[1:]:
            if there_is_overlap(interval, result[-1]):
                result[-1] = [
                    min(result[-1][0], interval[0]),
                    max(result[-1][1], interval[1]),
                ]
            else:
                result.append(interval)
        return result


s = Solution()
print(s.merge(intervals=[[1, 4], [2, 3]]))
