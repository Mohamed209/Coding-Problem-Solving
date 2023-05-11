# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        max_vow = cur_vow = 0
        for i, c in enumerate(s):
            if c in vowels:
                cur_vow += 1
            if i >= k and s[i - k] in vowels:
                cur_vow -= 1
            max_vow = max(max_vow, cur_vow)
        return max_vow
