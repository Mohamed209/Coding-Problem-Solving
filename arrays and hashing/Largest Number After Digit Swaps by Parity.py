# https://leetcode.com/problems/largest-number-after-digit-swaps-by-parity/
class Solution:
    def largestInteger(self, num: int) -> int:
        numdigits = [int(i) for i in str(num)]
        even = []
        odd = []
        for digit in numdigits:
            if digit % 2 == 0:
                even.append(digit)
            else:
                odd.append(digit)
        even.sort(reverse=True)
        odd.sort(reverse=True)
        print(even, odd)
        res = []
        evenptr = 0
        oddptr = 0
        for digit in numdigits:
            if digit % 2 == 0:
                res.append(even[evenptr])
                evenptr += 1
            else:
                res.append(odd[oddptr])
                oddptr += 1
        return int("".join([str(n) for n in res]))


s = Solution()
print(s.largestInteger(65875))
