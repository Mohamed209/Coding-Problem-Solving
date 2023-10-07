# https://leetcode.com/problems/reverse-only-letters/description/
from string import ascii_letters


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        left, right = 0, len(s) - 1
        sl = list(s)  # to make item assignment easy
        eng_letters = set(ascii_letters)  # for O(1) search
        while left < right:
            if s[left] in eng_letters and s[right] in eng_letters:
                # swap and advance pointers
                tmp = sl[left]
                sl[left] = sl[right]
                sl[right] = tmp
                left += 1
                right -= 1
            else:
                if sl[left] not in eng_letters:
                    left += 1
                if sl[right] not in eng_letters:
                    right -= 1
        return "".join(c for c in sl)


s = Solution()
print(s.reverseOnlyLetters(s="Test1ng-Leet=code-Q!"))
