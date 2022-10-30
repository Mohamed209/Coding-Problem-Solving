# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    cache = {}

    @staticmethod
    def dfs(nums: tuple[int], max_loot=0):
        if nums in Solution.cache:
            return Solution.cache[nums]
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums)
        """
        now ,for me as professional theif :D , which is better : 
        1- steal current house (nums[0]) + recurse again on houses starting from my starting point+2
        2- steal next house (nums[1]) + recurse again on houses starting from my starting point+3
        """
        max_loot += max(nums[0]+Solution.dfs(nums[2:], max_loot),
                        nums[1]+Solution.dfs(nums[3:]), max_loot)
        Solution.cache[tuple(nums)] = max_loot
        return max_loot

    def rob(self, nums: List[int]) -> int:
        # convert nums to tuple , to be used as key in caching dict (apply memoaization)
        return Solution.dfs(tuple(nums))


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([1, 2, 3, 1]))
