# https://leetcode.com/problems/removing-stars-from-a-string/
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != "*":
                stack.append(s[i])
            elif s[i] == "*":
                stack.pop()
        return "".join([c for c in stack])


s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
