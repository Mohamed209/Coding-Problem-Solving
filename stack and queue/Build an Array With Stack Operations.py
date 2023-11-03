# https://leetcode.com/problems/build-an-array-with-stack-operations
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack_operations = []
        # convert target to set() datastructure for O(1) search , since it is strictly incrasing
        last_num_in_target = target[-1]
        target = set(target)
        for i in range(1, n + 1):
            if i not in target:
                stack_operations.extend(["Push", "Pop"])
            else:
                stack_operations.append("Push")
            if i == last_num_in_target:
                return stack_operations


s = Solution()
s.buildArray(target=[1], n=3)
