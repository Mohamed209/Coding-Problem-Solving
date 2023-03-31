# https://www.lintcode.com/problem/663/
from typing import List


class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """

    def dfs(
        self, r: int, c: int, rooms: List[List[int]], visited: set, distance: int
    ) -> None:
        # base cases
        if (
            r < 0
            or r >= len(rooms)
            or c < 0
            or c >= len(rooms[0])
            or rooms[r][c] == -1
            or (r, c) in visited
        ):
            return
        # dfs in 4 directions
        visited.add((r, c))
        rooms[r][c] = min(
            rooms[r][c], distance
        )  # from current gate which is minimum , distance from the current gate or distance set by another gate
        self.dfs(r - 1, c, rooms, visited, distance + 1)
        self.dfs(r + 1, c, rooms, visited, distance + 1)
        self.dfs(r, c - 1, rooms, visited, distance + 1)
        self.dfs(r, c + 1, rooms, visited, distance + 1)

    def walls_and_gates(self, rooms: List[List[int]]) -> None:
        # write your code here
        rows = len(rooms)
        cols = len(rooms[0])
        visited = set()
        # start dfs from any gate
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    self.dfs(r, c, rooms, visited, 0)
                    visited.clear()
        return


s = Solution()
s.walls_and_gates(
    [
        [2147483647, -1, 0, 2147483647],
        [2147483647, 2147483647, 2147483647, -1],
        [2147483647, -1, 2147483647, -1],
        [0, -1, 2147483647, 2147483647],
    ]
)
s.walls_and_gates([[0, -1], [2147483647, 2147483647]])
