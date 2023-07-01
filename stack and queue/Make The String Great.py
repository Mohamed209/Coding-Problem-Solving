# https://leetcode.com/problems/make-the-string-great/
import string


class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        asci_lower = set(string.ascii_lowercase)
        asci_upper = set(string.ascii_uppercase)
        for char in s:
            if len(stack) == 0:
                stack.append(char)
            else:
                # two possibilities
                if (
                    stack[-1] in asci_lower
                    and char in asci_upper
                    and stack[-1] == char.lower()
                ) or (
                    stack[-1] in asci_upper
                    and char in asci_lower
                    and stack[-1] == char.upper()
                ):
                    stack.pop()
                else:
                    stack.append(char)
        return "".join(c for c in stack)
