# https://leetcode.com/problems/maximum-69-number/description/
class Solution:
    def maximum69Number(self, num: int) -> int:
        # convert to str for faster iteration
        numstr = [c for c in str(num)]
        # gready thinking should scan the array from left to right
        # and flip the first 6
        for i in range(len(numstr)):
            if numstr[i] == "6":
                numstr[i] = "9"
                break
        return int("".join(c for c in numstr))
