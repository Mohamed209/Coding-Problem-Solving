# https://leetcode.com/problems/01-matrix/
from typing import List
from collections import deque


class Solution:
    @staticmethod
    def bfs(i, j, matrix):
        q = deque()
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q.append(((i, j), 0))
        while q:
            # search level neighbours
            for _ in range(len(q)):
                coords, d = q.popleft()
                if matrix[coords[0]][coords[1]] == 0:
                    return d
                visited.add(coords)
                # investiagte neighbours
                for dir in dirs:
                    newX, newY = coords[0]+dir[0], coords[1]+dir[1]
                    # within bounds:
                    if newX >= 0 and newX <= len(matrix)-1 and \
                            newY >= 0 and newY <= len(matrix[0])-1:
                        # not seen:
                        if (newX, newY) not in visited:
                            q.append(((newX, newY), d+1))

    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    d = Solution.bfs(i, j, matrix)  # d = closest dist to a 0
                    matrix[i][j] = d  # update M with d
        return matrix


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))

#passed basic test cases only