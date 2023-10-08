from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if nums[high] >= nums[mid]:
                # we are lucky since there is no rotation detected
                # if x is greater, ignore left half
                if nums[mid] < target or target < nums[low]:
                    low = mid + 1
                # if x is smaller, ignore right half
                elif nums[mid] > target:
                    high = mid - 1
                # means x is present at mid
                else:
                    return mid
            else:
                # rotation detected , so we reverse the standard binary search algorithm
                # if x is greater, ignore right half
                if nums[mid] < target:
                    high = mid - 1
                # if x is smaller, ignore left half
                elif nums[mid] > target:
                    low = mid + 1
                # means x is present at mid
                else:
                    return mid
        # if we reach here, then the element was not present
        return -1


s = Solution()
print(s.search(nums=[3, 5, 1], target=3))
