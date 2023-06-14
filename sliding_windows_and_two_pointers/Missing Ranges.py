# https://www.lintcode.com/problem/641/
from typing import List


class Solution:
    """
    @param nums: a sorted integer array
    @param lower: An integer
    @param upper: An integer
    @return: a list of its missing ranges
    """

    def find_missing_ranges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        # write your code here
        def format(a, b):
            if a + 1 == b - 1:
                return str(b - a)
            return str(a + 1) + "->" + str(b - 1)

        if len(nums) == 0:
            return [format(lower - 1, upper + 1)]
        result = []
        if nums[0] != lower:
            result.append(format(lower, nums[0]))
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] > 1:
                result.append(format(nums[i], nums[i + 1]))
        if nums[-1] != upper:
            result.append(format(nums[-1], upper + 1))
        return result


s = Solution()
print(s.find_missing_ranges(nums=[0, 1, 3, 50, 75], lower=0, upper=99))
print(s.find_missing_ranges(nums=[0, 1, 2, 3, 7], lower=0, upper=7))
print(s.find_missing_ranges(nums=[], lower=1, upper=5))
