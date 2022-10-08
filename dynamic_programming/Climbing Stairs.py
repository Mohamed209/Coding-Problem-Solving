# https://leetcode.com/problems/climbing-stairs/

class Solution:
    cache = {}

    def climbStairs(self, n: int) -> int:
        if n in Solution.cache:
            return Solution.cache[n]
        if n in [0, 1]:
            return 1
        result = self.climbStairs(n-1)+self.climbStairs(n-2)
        Solution.cache[n] = result
        return result
