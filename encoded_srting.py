# problem : https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1379/
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ''
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                temps = ''
                while stack and stack[-1] != '[':
                    temps = stack.pop()+temps
                stack.pop()
                multi = ''
                while stack and stack[-1].isdigit():
                    multi = stack.pop()+multi
                multi = int(multi)
                temps = temps*multi
                stack.append(temps)

        return "".join(stack)
