# https://leetcode.com/problems/find-unique-binary-string/description/
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        int_nums = [int(x, 2) for x in nums]
        int_nums.sort()
        print(int_nums)
        if int_nums[0] != 0:
            return "0" * len(nums)
        """
        convert nums to array of integers then sort it
        after sorting , the ideal situation is at any index i in range[0,len(int_nums)-1]
        int_nums[i+1]-int_nums[i]==1
        """
        for i in range(0, len(int_nums) - 1):
            if int_nums[i + 1] - int_nums[i] != 1:
                return bin(int_nums[i] + 1)[2:].zfill(len(nums))
        return bin(int_nums[-1] + 1)[2:].zfill(len(nums))
