# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        left, right = 0, 2
        max_digit = ""
        while right < len(num):
            if num[left] == num[left+1] == num[left+2]:
                max_digit = max(max_digit, num[left])
                # jump three steps one time to check next window
                left += 3
                right += 3
            else:
                # keep move the sliding window one step forward
                left += 1
                right += 1
        if max_digit == "":
            return ""
        return max_digit*3


s = Solution()
print(res for res in [s.largestGoodInteger("222"), s.largestGoodInteger(
    "6777133339"), s.largestGoodInteger("2300019"), s.largestGoodInteger(num="42352338")])
