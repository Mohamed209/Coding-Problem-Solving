# https://leetcode.com/problems/maximum-units-on-a-truck/
from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # greedy thinking should give priority to boxes with higher number of units
        boxTypes = sorted(boxTypes, key=lambda x: x[1])
        current_capacity, max_units = truckSize, 0
        while current_capacity > 0:
            if not boxTypes:  # if we loaded all boxes to the truck
                return max_units  # return what max_units computed so far
            boxes, units = boxTypes.pop()  # pop next high priority boxtype
            current_capacity -= boxes  # reduce current capacity by boxes
            if current_capacity < 0:
                boxes += current_capacity  # need to fit in trucksize
            max_units += boxes * units
        return max_units


s = Solution()
print(s.maximumUnits(boxTypes=[[1, 3], [2, 2], [3, 1]], truckSize=4))
print(s.maximumUnits(boxTypes=[[5, 10], [2, 5], [4, 7], [3, 9]], truckSize=10))
