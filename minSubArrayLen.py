# problem : https://leetcode.com/problems/minimum-size-subarray-sum/
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        s = 0
        result = 10**5
        for i in range(len(nums)):
            s+=nums[i]
            while s >= target:
                result=min(i-left+1,result)
                s-=nums[left]
                left+=1
        if result==10**5:
            return 0
        else:
            return result