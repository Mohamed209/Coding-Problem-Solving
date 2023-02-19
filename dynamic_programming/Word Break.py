# https://leetcode.com/problems/word-break/
from typing import List

# check images/canConstruct.png , images/canSonstructMemo.png for tree sketch


class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        if s in self.cache:
            return self.cache[s]
        for word in wordDict:
            new_subword = s.removeprefix(word)
            # if removeprefix method returned the same string , this means that (word) is not prefix of (s)
            if len(new_subword) == len(s):
                continue  # move and try next word from wordDict , as current word is not prefix of s
            if self.wordBreak(new_subword, wordDict):
                self.cache[new_subword] = True
                return True
        self.cache[new_subword] = False
        return False


s = Solution()
print(s.wordBreak("applepie", ["pie", "pear", "apple", "peach"]))
