# problem : https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1153/
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftptr=0
        rightptr=len(numbers)-1
        while(leftptr<=rightptr):
            if numbers[leftptr]+numbers[rightptr]>target:
                rightptr-=1
            elif numbers[leftptr]+numbers[rightptr]<target:
                leftptr+=1
            else:
                return [leftptr+1,rightptr+1]