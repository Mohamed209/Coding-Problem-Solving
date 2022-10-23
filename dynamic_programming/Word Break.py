# https://leetcode.com/problems/word-break/
from typing import List


class Solution:
    cache = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0:
            return True
        if s in Solution.cache:
            return Solution.cache[s]
        for word in wordDict:
            new_subword = s.removeprefix(word)
            # if removeprefix method returned the same string , this means that (word) is not prefix of (s)
            if len(new_subword) == len(s):
                continue  # move and try next word from wordDict , as current word is not prefix of s
            if self.wordBreak(new_subword, wordDict):
                Solution.cache[new_subword] = True
                return True
        Solution.cache[new_subword] = False
        return False


s = Solution()
print(s.wordBreak("applepie", ["pie", "pear", "apple", "peach"]))
