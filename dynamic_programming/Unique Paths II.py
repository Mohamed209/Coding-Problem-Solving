# https://leetcode.com/problems/unique-paths-ii/
from functools import cache
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        @cache
        def dfs(row: int, col: int):
            # hey robot listen me carefully , when you are going out of bounds or you find an obstacle , please stop and switch to the other option
            if row >= total_rows or col >= total_cols or obstacleGrid[row][col] == 1:
                return 0
            # if you reach the final destination , good job just flag me with 1
            # listen carefully , do not step again on valid cell that lead you -in the past- to the destination , this is waste of time this why @cache is added to the function dfs
            if row == total_rows - 1 and col == total_cols - 1:
                # the robot made it to the destination , we found one unique path
                return 1
            # from every starting cell (row,col) the robot has two options
            res = dfs(row, col + 1) + dfs(
                row + 1, col
            )  # first option move to the right dfs(row, col+1) , second option move down dfs(row+1,col)
            return res

        total_rows = len(obstacleGrid)
        total_cols = len(obstacleGrid[0])
        return dfs(0, 0)


s = Solution()
print(s.uniquePathsWithObstacles(obstacleGrid=[[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
print(
    s.uniquePathsWithObstacles(
        obstacleGrid=[
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1],
            [0, 0, 0, 1, 0],
            [0, 0, 1, 0, 0],
        ]
    )
)
