from bisect import bisect_left
from typing import List


class Solution:
    # def rotBinarySearch(self, left, right, nums, target):
    #     if right >= left:
    #         mid = (right - left) // 2 + left
    #         if target == nums[mid]:
    #             return mid
    #         # if it was ordinary array we would go search in right area next to mid
    #         # we need to modify the algorithm to handle possible rotations
    #         elif target > nums[mid]:
    #             if (
    #                 nums[right] < nums[mid]
    #             ):  # rotation detected , search in opposite section
    #                 return self.rotBinarySearch(left, mid - 1, nums, target)
    #             else:
    #                 return self.rotBinarySearch(mid + 1, right, nums, target)
    #         else:
    #             if nums[right] < nums[mid]:
    #                 # rotation detected , search in opposite section
    #                 return self.rotBinarySearch(mid + 1, right, nums, target)
    #             else:
    #                 return self.rotBinarySearch(left, mid - 1, nums, target)
    #     else:
    #         return -1

    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(a, x):
            i = bisect_left(a, x)
            if i != len(a) and a[i] == x and a[i + 1] < x:
                return i
            else:
                return -1

        # return self.rotBinarySearch(
        #     left=0, right=len(nums) - 1, nums=nums, target=target
        # )


s = Solution()
print(s.search(nums=[3, 5, 1], target=3))
