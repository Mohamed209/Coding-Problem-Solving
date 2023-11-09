# https://leetcode.com/problems/count-number-of-homogenous-substrings
class Solution:
    def countHomogenous(self, s: str) -> int:
        left, right = 0, 0
        cnt = 0
        while right < len(s):
            if s[right] != s[left]:
                n = right - left
                cnt += n * (n + 1) // 2
                left = right
            else:
                right += 1
        lastn = right - left
        cnt += lastn * (lastn + 1) // 2
        return cnt


s = Solution()
s.countHomogenous(s="abbcccaa")
