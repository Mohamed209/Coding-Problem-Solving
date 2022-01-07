# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left_ptr = 0
        right_ptr = 0
        max_len = 0
        char_set = {}
        while right_ptr < len(s) and left_ptr < len(s):
            if s[right_ptr] not in char_set:
                char_set[s[right_ptr]] = right_ptr
                right_ptr += 1
                max_len = max(max_len, right_ptr - left_ptr)
            elif s[right_ptr] in char_set:
                char_set.pop(s[left_ptr])
                left_ptr += 1
        return max_len
