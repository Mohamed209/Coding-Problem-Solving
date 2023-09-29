# https://leetcode.com/problems/multiply-strings/description/
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        str2int_map = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
        }

        def str2int(x: str):
            res = 0
            for i in range(len(x)):
                res += str2int_map[x[i]] * (10 ** (len(x) - 1 - i))
            return res

        return str(str2int(num1) * str2int(num2))


s = Solution()
s.multiply(num1="123", num2="456")
