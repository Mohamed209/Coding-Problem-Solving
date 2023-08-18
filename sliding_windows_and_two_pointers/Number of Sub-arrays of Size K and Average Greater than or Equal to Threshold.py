# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        current_window_sum = -1
        result = 0
        left = 0
        right = k - 1
        while right < len(arr):
            if current_window_sum == -1:
                # first window
                current_window_sum = sum(arr[left : right + 1])
            current_window_avg = current_window_sum // k
            if current_window_avg >= threshold:
                # print just for debugging
                # print(arr[left : right + 1])
                result += 1
            # move sliding window to the left one step
            current_window_sum -= arr[left]
            left += 1
            right += 1
            if right == len(arr):
                # reached last window
                break
            current_window_sum += arr[right]
        return result


s = Solution()
print(s.numOfSubarrays(arr=[2, 2, 2, 2, 5, 5, 5, 8], k=3, threshold=4))
