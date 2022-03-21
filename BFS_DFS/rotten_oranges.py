# problem : https://leetcode.com/problems/rotting-oranges/
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time = 0
        fresh_count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh_count += 1
                elif grid[i][j] == 2:
                    q.append([i, j])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        while q and fresh_count > 0:
            for _ in range(len(q)):
                i, j = q.popleft()
                # search all adjacent cells
                for dr, dc in directions:
                    row, col = dr+i, dc+j
                    if (row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    fresh_count -= 1
                    q.append([row, col])
            time += 1
        if fresh_count == 0:
            return time
        else:
            return -1
