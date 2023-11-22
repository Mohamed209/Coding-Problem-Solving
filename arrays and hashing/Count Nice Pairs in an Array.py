# https://leetcode.com/problems/count-nice-pairs-in-an-array
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        """
        nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])
        can be converted into -->
        nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

        so let us loop the array and compute for every index i
        nums[i] - rev(nums[i]) and save the result in hash_set

        if we find again the same value at other i_next , where i_next > i
        this simulates finding nums[j] - rev(nums[j])
        """
        diffs_map = {}
        cnt = 0
        mod = 10**9 + 7
        for i in range(len(nums)):
            rev = int(str(nums[i])[::-1])
            diff = nums[i] - rev
            if diff in diffs_map:
                diffs_map[diff] += 1
                cnt += diffs_map[diff]
            else:
                diffs_map[diff] = 0
        return cnt % mod


s = Solution()
s.countNicePairs(nums=[13, 10, 35, 24, 76])
