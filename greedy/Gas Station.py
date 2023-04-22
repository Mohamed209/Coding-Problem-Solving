# https://leetcode.com/problems/gas-station/
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        thinking greedy , let us start at the gas station that has lowest cost move from and corresponds to maximum gas loot
        then move to station with second lowest cost and second biggest gas loot , then to station with third lowest cost ..... and so on
        """
        sorted_cost = [(x, y, i) for i, (x, y) in enumerate(zip(cost, gas))]
        sorted_cost = sorted(sorted_cost, key=lambda x: (x[0], -x[1]))
        current_tank = gas[sorted_cost[0][2]]
        for idx, sc in enumerate(sorted_cost):
            if idx == len(sorted_cost) - 1:
                if current_tank - cost[sc[2]] < 0:
                    return -1
                current_tank = current_tank - cost[sc[2]] + gas[sorted_cost[0][2]]
            else:
                current_tank = current_tank - cost[sc[2]] + gas[sorted_cost[idx + 1][2]]
        return sorted_cost[0][2]


s = Solution()
print(s.canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
print(s.canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))
print(s.canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]))
