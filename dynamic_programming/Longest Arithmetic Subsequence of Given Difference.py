# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

# TLE (tried as much I could)
from typing import List


class Solution:
    def __init__(self) -> None:
        self.cache = {}  # memoization

    def dfs(self, arr: List[int], idx: int, difference: int) -> int:
        if (idx, arr[idx]) in self.cache:
            return self.cache[(idx, arr[idx])]
        if idx > len(arr):
            return 0
        # search in hash set version in the subarray from [i+1:] for arr[i]+difference
        if idx == len(arr) or difference + arr[idx] not in set(arr[idx + 1 :]):
            self.cache[(idx, arr[idx])] = 1
            return 1
        """
        if we reached here 
        this is for sure the start of one possible arithmetic subarray
        all we need to do is to recursively hop into this found number in the subarray arr[idx+1:]
        """
        newidx = idx + arr[idx + 1 :].index(difference + arr[idx]) + 1
        res = 1 + self.dfs(arr, newidx, difference)
        self.cache[(idx, arr[idx])] = res
        return res

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        possible_paths_lens = []
        for i in range(len(arr)):
            possible_paths_lens.append(self.dfs(arr, i, difference))
        return max(possible_paths_lens)


s = Solution()
print(s.longestSubsequence(arr=[1, 5, 7, 8, 5, 3, 4, 2, 1], difference=-2))
