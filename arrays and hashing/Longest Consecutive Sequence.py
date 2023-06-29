# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        visited_path = set()
        longest = 0
        for i in range(len(nums)):
            longest_left, longest_right = 0, 0
            numleft = nums[i] + 1
            # search for consecutives (as far as we can reach) to the left of current num
            # but take care do not visit again a number already visited in previous path
            while numleft in nums_set and numleft not in visited_path:
                longest_left += 1
                visited_path.add(numleft)
                numleft += 1
            # search for consecutives (as far as we can reach) to the right of current num
            # but take care do not visit again a number already visited in previous path
            numright = nums[i] - 1
            while numright in nums_set and numright not in visited_path:
                longest_right += 1
                visited_path.add(numright)
                numright -= 1
            longest = max(longest, longest_left + longest_right + 1)
        return longest


s = Solution()
print(s.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
