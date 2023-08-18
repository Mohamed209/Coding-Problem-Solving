# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq_map = {}
        for i in range(len(nums)):
            if nums[i] not in freq_map:
                freq_map[nums[i]] = i  # save first occurance
            else:
                # we have met this number before at some index i
                # now we are at index j let us check if this pair is valid
                if abs(freq_map[nums[i]] - i) <= k:
                    return True
                else:
                    # we need to save the new position of the new number , check case [1,0,1,1]
                    freq_map[nums[i]] = i
        return False


s = Solution()
print(s.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
