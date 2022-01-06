class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left_ptr = 0
        right_ptr = 0
        max_len = 0
        char_set = set()
        while right_ptr < len(s):
            if s[right_ptr] not in char_set:
                char_set.add(s[right_ptr])
                right_ptr += 1
            elif s[right_ptr] in char_set:
                new_max = right_ptr - left_ptr
                max_len = max(new_max, max_len)
                left_ptr = right_ptr
                right_ptr += 1
        if max_len == 0:
            return len(char_set)
        return max_len


s = Solution()
print(s.lengthOfLongestSubstring("abc"))
