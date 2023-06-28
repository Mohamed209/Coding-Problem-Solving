# https://leetcode.com/problems/product-of-array-except-self/description/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums)
        postfix_product = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        for j in range(len(nums) - 2, -1, -1):
            postfix_product[j] = postfix_product[j + 1] * nums[j + 1]
        res = []
        for pre, post in zip(prefix_product, postfix_product):
            res.append(pre * post)
        return res


s = Solution()
print(s.productExceptSelf([1, 2, 3, 4]))
