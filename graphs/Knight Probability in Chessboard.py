# https://leetcode.com/problems/knight-probability-in-chessboard/description/
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        @cache
        def dfs(row: int, col: int, rem_moves: int) -> int:
            if row < 0 or row >= n or col < 0 or col >= n:
                return 0
            # good :) , we are still inside the chess board and avoided closed loops
            # what if we consumed all k moves , this for sure is a valid path
            if rem_moves == 0:
                return 1
            # start dfs for the cell 8 neighbours
            neigbours_coords = [
                (row - 1, col + 2),
                (row - 1, col - 2),
                (row + 1, col + 2),
                (row + 1, col - 2),
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row + 2, col + 1),
                (row + 2, col - 1),
            ]
            res = 0
            for coord in neigbours_coords:
                res += dfs(coord[0], coord[1], rem_moves - 1)
            return res

        return dfs(row, column, rem_moves=k) / 8**k


s = Solution()
print(s.knightProbability(n=3, k=2, row=0, column=0))
print(s.knightProbability(n=1, k=0, row=0, column=0))
