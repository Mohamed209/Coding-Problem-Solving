# https://leetcode.com/problems/permutation-in-string/
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sum_s1 = 0
        for c in s1:
            sum_s1 += ord(c)
        # search s2 for this sum using sliding windows
        left_ptr = 0
        right_ptr = 1
        while right_ptr < len(s2) and left_ptr < len(s2):
            current_window_sum = sum([ord(c) for c in s2[left_ptr:right_ptr+1]])
            if current_window_sum == sum_s1:
                return True
            elif current_window_sum < sum_s1:
                right_ptr += 1
            else:
                left_ptr += 1
        return False


s = Solution()
print(s.checkInclusion("ab", "ba"))
