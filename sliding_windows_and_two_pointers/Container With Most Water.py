# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # initial largest window
        left = 0
        right = len(height) - 1
        max_area = 0
        while right != left:
            max_area = max(max_area, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]:
                """
                moving right to the left area will have no effect and will deviate us from maximizng the area
                because height is till height[left] and we are decreasing the width so in this case we are minimzing the area
                better option now is to move the left to the right
                """
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
print(s.maxArea(height=[1, 2, 1]))
print(s.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
