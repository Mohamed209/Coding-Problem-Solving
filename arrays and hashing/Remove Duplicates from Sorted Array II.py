# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
from collections import Counter
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        freq = dict(sorted(Counter(nums).items()))
        idx_tofill = 0
        for key in freq:
            if freq[key] >= 2:
                for _ in range(2):
                    nums[idx_tofill] = key
                    idx_tofill += 1
            else:
                nums[idx_tofill] = key
                idx_tofill += 1
        return idx_tofill


s = Solution()
print(s.removeDuplicates(nums=[0, 0, 1, 1, 1, 1, 2, 3, 3]))
