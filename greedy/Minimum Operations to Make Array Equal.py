# https://leetcode.com/problems/minimum-operations-to-make-array-equal/description/
class Solution:
    def minOperations(self, n: int) -> int:
        nums = [(2 * i + 1) for i in range(n)]
        # print("nums: ", nums)
        avg = (nums[0] + nums[-1]) // 2  # mean of odd sequence
        # print("avg: ", avg)
        steps = 0
        for i in range(n):
            if nums[i] >= avg:
                break
            steps += avg-nums[i]
        return steps


s = Solution()
s.minOperations(n=6)
