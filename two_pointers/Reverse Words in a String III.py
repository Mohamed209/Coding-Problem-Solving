# https://leetcode.com/problems/reverse-words-in-a-string-iii/
from typing import List


def reverseString(s: List[str]) -> None:
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
        left_ptr += 1
        right_ptr -= 1
    return s


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            word_l = [c for c in words[i]]
            word = reverseString(word_l)
            words[i] = ''.join([c for c in word])
        return ' '.join([word for word in words])
