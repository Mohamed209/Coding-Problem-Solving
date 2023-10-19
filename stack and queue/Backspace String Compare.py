# https://leetcode.com/problems/backspace-string-compare/description
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def handle_white_spaces(text: str):
            stack = []
            for char in text:
                if char == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(c for c in stack)

        return handle_white_spaces(s) == handle_white_spaces(t)


s = Solution()
s.backspaceCompare(s="ab##", t="c#d#")
