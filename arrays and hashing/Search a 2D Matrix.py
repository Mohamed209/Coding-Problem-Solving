# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


def binary_search(arr, low, high, x):

    # Check base case
    if high >= low:
        mid = (high + low) // 2
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        # Element is not present in the array
        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        best_row = 0
        last_row2search = 0
        # first reduce search space
        for r in range(rows):
            idx = rows-r-1
            if target < matrix[idx][0]:
                continue
            elif target == matrix[idx][0]:
                return True
            else:
                last_row2search = idx
                break
        # second find best row to search
        for r in range(last_row2search+1):
            if target > matrix[r][-1]:
                continue
            elif target == matrix[r][-1]:
                return True
            else:
                best_row = r
                break
        if binary_search(matrix[best_row], 1, len(matrix[best_row])-1, target):
            return True
        else:
            return False
