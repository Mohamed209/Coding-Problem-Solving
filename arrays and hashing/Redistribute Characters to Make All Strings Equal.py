# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal
from typing import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        if len(words) == 1:
            return True
        bag_of_chars = Counter("".join(word for word in words))
        for char in bag_of_chars:
            if bag_of_chars[char] % len(words) != 0:
                return False
        return True


s = Solution()
s.makeEqual(words=["abc", "aabc", "bc"])
