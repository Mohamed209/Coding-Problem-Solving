# https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
from typing import List


class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        """
        let running_sum is a variable of type List[int] is the running sum of nums
        let x = min(running_sum)
        if x>0 simply return 1 as we are sure there is no loose (negative) during the traversal
        but if x<0 , then simply to be in the safe side and not to dip below 0 we should start with a value
        y where y=abs(x)+1
        """
        running_sum = [nums[0]]
        for i in range(1, len(nums)):
            running_sum.append(running_sum[-1] + nums[i])
        x = min(running_sum)
        if x > 0:
            return 1
        else:
            return abs(x) + 1


s = Solution()
print(s.minStartValue(nums=[2, 3, 5, -5, -1]))  # [2,5,10,5,4]
print(s.minStartValue(nums=[-3, 2, -3, 4, 2]))  # [-3,-1,-4,0,2]
