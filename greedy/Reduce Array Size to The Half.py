# https://leetcode.com/problems/reduce-array-size-to-the-half/
from collections import Counter, deque
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        greedy thinking should focus on popping high frequency numbers from the array until its size is reduced by helf
        """
        freq_dict = dict(
            sorted(Counter(arr).items(), key=lambda x: x[1], reverse=True)
        )  # sorted by frequency descending order
        priority_q = deque()
        result = set()
        # create a priority queue giving priority for high frequency numbers
        for key in freq_dict:
            [priority_q.appendleft(key) for _ in range(freq_dict[key])]
        while len(priority_q) > len(arr) // 2:
            result.add(priority_q.pop())
        return len(result)


s = Solution()
print(s.minSetSize(arr=[9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]))
