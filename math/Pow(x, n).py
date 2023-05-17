# https://leetcode.com/problems/powx-n/
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1.0:  # 1 power to any n is 1
            return 1
        # -1^n = 1 if n is even
        elif x == -1.0 and n % 2 == 0:
            return 1
        # -1^n = -1 if n is odd
        elif x == -1 and n % 2 != 0:
            return -1
        # 0^n = 0
        elif round(x, 1) == 0.0:
            return 0
        res = 1
        if n == 0.0:
            # x^0=1
            return res
        elif n > 0:
            for _ in range(n):
                res *= x
            return res
        else:
            for _ in range(-n):
                res *= x
                if 1 / res == 0.0:
                    return 0
            return 1 / res


s = Solution()
s.myPow(2.00000, -2)
