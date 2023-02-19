# https://leetcode.com/problems/decode-ways/
class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def numDecodings(self, s: str) -> int:
        if s in self.cache:
            return self.cache[s]
        if len(s) == 1 and s[0] != "0" or s in ["10", "20"]:
            # base case , I found a way to decode the string
            return 1
        elif len(s) == 2 and s[0] != "0" and int(s) <= 26:
            # base case , I found a way to decode the string
            return 2
        elif len(s) == 0 or s[0] == "0":
            # base case , dead end
            return 0
        """
        two options:
        1- take first char , then recurse again for remaining substring
        2- take first two , then also recurse again for remaining substring
        """
        if len(s) >= 2 and int(s[:2]) > 26:
            ways = self.numDecodings(s[1:])
        else:
            ways = self.numDecodings(s[1:])+self.numDecodings(s[2:])
        self.cache[s] = ways
        return ways


s = Solution()
print(s.numDecodings("12120"))
