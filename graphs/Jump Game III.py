# https://leetcode.com/problems/jump-game-iii/
from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def dfs(arr: List[int], start: int, visited: set) -> bool:
            if start >= len(arr) or start < 0 or start in visited:
                return False
            if arr[start] == 0:
                return True
            visited.add(start)
            return dfs(arr, start + arr[start], visited) or dfs(
                arr, start - arr[start], visited
            )

        visited = set()
        return dfs(arr, start, visited)


s = Solution()
print(s.canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
