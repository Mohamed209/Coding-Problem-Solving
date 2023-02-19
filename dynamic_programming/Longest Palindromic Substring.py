# https://leetcode.com/problems/longest-palindromic-substring/
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
        """
        res = 0
        substr = ""
        for i in range(len(s)):
            # assume current char is the center char
            l, r = i, i
            # expand window left and right with one char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res:
                    res = r-l+1
                    substr = s[l:r+1]
                l -= 1
                r += 1
            # assume current two chars in the middle is the center char
            l, r = i, i+1
            # expand window left and right with one char
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 > res:
                    res = r-l+1
                    substr = s[l:r+1]
                l -= 1
                r += 1
        return substr


s = Solution()
print(s.longestPalindrome("babad"))
print(s.longestPalindrome("cbbd"))
