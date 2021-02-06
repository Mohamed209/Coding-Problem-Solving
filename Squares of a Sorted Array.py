# problem : 
def sortedSquares(nums):
        result = [0]*len(nums)
        left=0
        right=len(nums)-1
        res_index=len(nums)-1
        while(left<=right):
            if abs(nums[left]) < abs(nums[right]):
                result[res_index]=nums[right]**2
                res_index-=1
                right-=1
            else:
                result[res_index]=nums[left]**2
                res_index-=1
                left+=1
        return result

sortedSquares([-4,-1,0,3,10])