# https://leetcode.com/problems/water-bottles/description/
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_max_drink = numBottles
        while numBottles >= numExchange:
            max_drink = numBottles // numExchange
            total_max_drink += max_drink
            remaining = numBottles % numExchange
            numBottles = max_drink + remaining
        return total_max_drink