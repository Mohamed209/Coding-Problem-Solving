# problem : https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums)==2:
            return min(nums)
        numsorted = sorted(nums)
        maxsum = 0
        for i in range(0,len(numsorted),2):
            maxsum+=numsorted[i]
        return maxsum