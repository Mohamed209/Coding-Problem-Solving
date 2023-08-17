# https://leetcode.com/problems/merge-strings-alternately/description/
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        left, right = 0, 0
        while left < len(word1) and right < len(word2):
            res += word1[left] + word2[right]
            left += 1
            right += 1
        # handle if any string longer than other
        if left == len(word1) and right < len(word2):
            res += word2[right:]
            return res
        elif right == len(word2) and left < len(word1):
            res += word1[left:]
            return res
        return res
