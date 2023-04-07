# https://leetcode.com/problems/01-matrix/
from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    def bfs(
        self, r: int, c: int, mat: List[List[int]], visited: set, level: int
    ) -> int:
        queue = deque()
        queue.appendleft((r, c))
        visited.add((r, c))
        while len(queue) > 0:
            for _ in range(len(queue)):
                start = queue.pop()
                directions = [
                    (start[0] - 1, start[1]),
                    (start[0] + 1, start[1]),
                    (start[0], start[1] - 1),
                    (start[0], start[1] + 1),
                ]
                for dir in directions:
                    if (
                        dir[0] < 0
                        or dir[0] >= len(mat)
                        or dir[1] < 0
                        or dir[1] >= len(mat[0])
                        or (dir[0], dir[1]) in visited
                    ):
                        continue
                    if mat[dir[0]][dir[1]] == 0:
                        return level
                    queue.appendleft((dir[0], dir[1]))
                    visited.add((dir[0], dir[1]))
            level += 1
        return 0

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        visited = set()
        result = deepcopy(mat)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    result[r][c] = self.bfs(r, c, mat, visited, level=1)
                    visited.clear()
        return result


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(
    s.updateMatrix(
        [
            [1, 0, 1, 1, 0, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
            [0, 0, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
            [0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1],
        ]
    )
)