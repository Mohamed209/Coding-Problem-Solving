# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def fib(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        if n in [1, 2]:
            return 1
        elif n == 0:
            return 0
        result = self.fib(n-1)+self.fib(n-2)
        self.cache[n] = result
        return result
