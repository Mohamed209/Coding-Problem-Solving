# https://leetcode.com/problems/reverse-string/
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_ptr = 0
        right_ptr = len(s)-1
        while(left_ptr <= right_ptr):
            # swap
            tmp = s[right_ptr]
            s[right_ptr] = s[left_ptr]
            s[left_ptr] = tmp
            # moving pointers
            left_ptr += 1
            right_ptr -= 1
        return s
