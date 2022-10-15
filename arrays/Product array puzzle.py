# https://www.geeksforgeeks.org/a-product-array-puzzle/
class Solution:
    def productExceptSelf(self, nums, n):
        # code here
        # let us find the total product of the array --> O(n)
        total_product = 1
        zeros_count = 0
        zeros_index = []
        for i in range(len(nums)):
            if nums[i] == 0:
                zeros_count += 1
                zeros_index.append(i)
                total_product *= 1
            else:
                total_product *= nums[i]
        if zeros_count >= 2:
            return [0 for _ in range(len(nums))]
        elif zeros_count == 1:
            P = [0 for _ in range(len(nums))]
            P[zeros_index[0]] = total_product
            return P
        # scan nums O(n) divide total_product by every num
        P = []
        for num in nums:
            P.append(total_product//num)
        return P
