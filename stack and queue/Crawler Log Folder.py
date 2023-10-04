# https://leetcode.com/problems/crawler-log-folder/description/
from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if log not in ["./", "../"]:
                stack.append(log)
            elif log == "../" and stack:
                stack.pop()
        return len(stack)


s = Solution()
s.minOperations(logs=["d1/", "d2/", "./", "d3/", "../", "d31/"])
