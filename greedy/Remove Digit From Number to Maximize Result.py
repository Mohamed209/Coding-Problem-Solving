# https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        numstr = [int(c) for c in number]
        idx_to_remove = len(numstr) - 1
        for i in range(len(numstr)):
            # greedy thinking should scan the array from left to right
            # if you land "digit" you should only remove it if its right neighbour is larger than it
            if numstr[i] == int(digit):
                if i == len(numstr) - 1:
                    idx_to_remove = i
                    break
                if numstr[i + 1] > numstr[i]:
                    idx_to_remove = i
                    break
                idx_to_remove = i
        return "".join(
            [str(num) for num in numstr[:idx_to_remove] + numstr[idx_to_remove + 1 :]]
        )


s = Solution()
print(s.removeDigit("73190", "7"))
