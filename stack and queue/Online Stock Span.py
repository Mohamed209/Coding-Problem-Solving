# https://leetcode.com/problems/online-stock-span/description/
class StockSpanner:
    def __init__(self):
        self.history = []  # history stack saved in decreasing order

    def next(self, price: int) -> int:
        span = 1
        while self.history and self.history[-1][0] <= price:
            _, prev_span = self.history.pop()
            span += prev_span
        self.history.append((price, span))
        return span


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
