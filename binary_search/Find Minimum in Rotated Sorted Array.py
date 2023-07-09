# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums is sorted but rotated then we shall make use of binary search
        left = 0
        right = len(nums) - 1

        def binary_search(left_index: int, right_index: int, nums: List[int]):
            while left_index < right_index:
                mid = (left_index + right_index) // 2
                if nums[right_index] < nums[mid]:
                    # this means the subarray right to the mid is the one that contains the min
                    # this means the right subarray originally was left to mid but came here as result of rotation
                    return binary_search(
                        left_index=mid + 1, right_index=right_index, nums=nums
                    )
                elif nums[right_index] >= nums[mid]:
                    # search in the left subarray
                    return binary_search(
                        left_index=left_index, right_index=mid, nums=nums
                    )
            return nums[left_index]

        return binary_search(left, right, nums)


s = Solution()
print(s.findMin([3, 1, 2]))
print(s.findMin(nums=[4, 5, 6, 7, 0, 1, 2]))
print(s.findMin(nums=[3, 4, 5, 1, 2]))
