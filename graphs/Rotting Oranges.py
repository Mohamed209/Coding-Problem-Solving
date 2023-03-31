# https://leetcode.com/problems/rotting-oranges/
# todo : fix later
from collections import deque
from typing import List


class Solution:
    @staticmethod
    def valid_cell(grid, r, c, visited):
        if (
            r < 0
            or r >= len(grid)
            or c < 0
            or c >= len(grid[0])
            or (r, c) in visited
            or grid[r][c] == 0
        ):
            return False
        return True

    def bfs(self, grid, r, c, visited, fresh_count):
        minutes = -1
        queue = deque()
        queue.appendleft((r, c))
        visited.add((r, c))
        while len(queue) > 0:
            for _ in range(len(queue)):  # for all neighbours
                current_position = queue.pop()
                rc, cc = current_position[0], current_position[1]
                cell = grid[rc][cc]
                directions = [(rc - 1, cc), (rc + 1, cc), (rc, cc - 1), (rc, cc + 1)]
                for dir in directions:
                    if Solution.valid_cell(grid, dir[0], dir[1], visited) and cell == 2:
                        grid[dir[0]][dir[1]] = 2  # neighbour will rot
                        fresh_count -= 1
                        visited.add((dir[0], dir[1]))
                        queue.appendleft(dir)
            minutes += 1
        return minutes if fresh_count == 0 else -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        # as it is really clear from problem description(images) that rotting happens on levels not depth
        # so let us use BFS
        visited = set()
        fresh_count = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh_count += 1
        return self.bfs(grid, 0, 0, visited, fresh_count)


s = Solution()
print(s.orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
s = Solution()
print(s.orangesRotting([[0, 2]]))
s = Solution()
print(s.orangesRotting([[1, 2]]))
