# https://leetcode.com/problems/palindromic-substrings
class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
        """
        cnt = 0
        for i in range(len(s)):
            # assume current char is the center char
            l, r = i, i
            # expand window left and right with one char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            # assume current two chars in the middle is the center char
            l, r = i, i+1
            # expand window left and right with one char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
        return cnt


s = Solution()
print(s.countSubstrings("abc"))
print(s.countSubstrings("aaa"))
