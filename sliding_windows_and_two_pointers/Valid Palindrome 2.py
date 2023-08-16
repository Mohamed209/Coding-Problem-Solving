# https://leetcode.com/problems/valid-palindrome-ii/
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                # simulate if del at right and del at left
                s1 = s[:left] + s[left + 1 :]  # del s[right]
                s2 = s[:right] + s[right + 1 :]  # del s[left]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False
            left += 1
            right -= 1
        return True


s = Solution()
print(s.validPalindrome("deeee"))
# radazr
