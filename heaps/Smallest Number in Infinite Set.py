# https://leetcode.com/problems/smallest-number-in-infinite-set
import heapq


class SmallestInfiniteSet:
    def __init__(self):
        self.infinite_set = [
            i for i in range(1, 1001)
        ]  # from problem constrains , 1 <= num <= 1000
        heapq.heapify(self.infinite_set)

    def popSmallest(self) -> int:
        return heapq.heappop(self.infinite_set)

    def addBack(self, num: int) -> None:
        if num not in self.infinite_set:
            heapq.heappush(self.infinite_set, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
obj = SmallestInfiniteSet()
obj.addBack(2)
obj.popSmallest()
obj.popSmallest()
obj.popSmallest()
obj.addBack(1)
obj.addBack(1)
obj.addBack(1)
obj.popSmallest()
obj.popSmallest()
obj.popSmallest()
