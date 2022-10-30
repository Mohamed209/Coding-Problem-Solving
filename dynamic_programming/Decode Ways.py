# https://leetcode.com/problems/decode-ways/
# revisit
class Solution:
    @staticmethod
    def dfs(s: str, index: int, cache: dict):
        if cache[index]:
            return cache[index]
        if index == len(s):
            return 1
        elif s[index] == "0":
            return 0
        result = Solution.dfs(s, index+1, cache)
        if index + 1 < len(s) and int(s[index:index+2]) <= 26:
            result += Solution.dfs(s, index+2, cache)
        cache[index] = result
        return result

    def numDecodings(self, s: str) -> int:
        cache = {i: None for i in range(len(s)+1)}
        return Solution.dfs(s, 0, cache)
