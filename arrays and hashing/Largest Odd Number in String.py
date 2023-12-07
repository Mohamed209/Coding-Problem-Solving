# https://leetcode.com/problems/largest-odd-number-in-string/description
class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds = {"1", "3", "5", "7", "9"}
        for i in reversed(range(len(num))):
            if num[i] in odds:
                return num[: i + 1]
        return ""


s = Solution()
s.largestOddNumber(num="52")
s.largestOddNumber(num="35427")
