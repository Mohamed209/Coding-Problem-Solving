# https://leetcode.com/problems/kth-largest-element-in-a-stream/
from typing import List

"""
as we deal with stream of data , so insert frequency is too high , and python lists are not optimized for too frequent inserts
we need another data structure optimized for that
another point we need some sort of queue with size k only , no need to save all the stream in a sorted way and get kth value from it
so it is clear that priority queue is the best DS to handle this problem ==> insert is LOG(N)
also sorted lists is valid and relatively fast solution ==> insert is LOG(N)
"""
from sortedcontainers import SortedList


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = SortedList(nums, lambda x: -x)
        self.k = k

    def add(self, val: int) -> int:
        self.nums.add(val)
        return self.nums[self.k - 1]


obj = KthLargest(3, [4, 5, 8, 2])
vals = [3, 5, 10, 9, 4]
for val in vals:
    print(obj.add(val))
obj = KthLargest(2, [0])
vals = [-1, 1, -2, -4, 3]
for val in vals:
    print(obj.add(val))
obj = KthLargest(3, [1, 1])
vals = [1, 1, 3, 3, 3, 4, 4, 4]
for val in vals:
    print(obj.add(val))
