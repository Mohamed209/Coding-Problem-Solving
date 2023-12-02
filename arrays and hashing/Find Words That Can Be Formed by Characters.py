# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
from typing import List
from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_dict = Counter(chars)
        length = 0
        for word in words:
            good_word = True
            word_dict = Counter(word)
            for key in word_dict:
                if (key not in chars_dict) or (
                    key in chars_dict and chars_dict[key] < word_dict[key]
                ):
                    good_word = False
                    break
            if good_word:
                length += len(word)
        return length


s = Solution()
s.countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach")
