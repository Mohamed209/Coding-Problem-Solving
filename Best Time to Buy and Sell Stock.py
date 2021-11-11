from typing import List

# problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[l] >= prices[r]:
                l = r
                r += 1
            elif prices[r] > prices[l]:
                # we found a profit window
                curprofit = prices[r]-prices[l]
                if curprofit > profit:
                    profit = curprofit
                r += 1
        return profit

s=Solution()
s.maxProfit([7,1,5,3,6,4])