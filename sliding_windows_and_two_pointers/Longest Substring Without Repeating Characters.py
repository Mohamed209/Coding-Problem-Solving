# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 1
        window_hash_search = {}
        window_hash_search[s[left]] = True
        length = 1
        while right < len(s):
            if s[right] not in window_hash_search:
                window_hash_search[s[right]] = True
                right += 1
                length = max(length, right - left)
            else:
                del window_hash_search[s[left]]
                left += 1
        return length
