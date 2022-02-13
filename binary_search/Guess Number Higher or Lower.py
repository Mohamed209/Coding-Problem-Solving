# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

# https://leetcode.com/problems/guess-number-higher-or-lower/
class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while left < right:
            mid = (right-left)//2+left
            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                right = mid-1
            else:
                left = mid+1
        return left
