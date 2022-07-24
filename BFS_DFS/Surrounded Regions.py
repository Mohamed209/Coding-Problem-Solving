# https://leetcode.com/problems/surrounded-regions/
from typing import List


class Solution:
    @staticmethod
    def dfs(r, c, board):
        if r < 0 or r == len(board) or c < 0 or c == len(board[0]) or board[r][c] in ["*", "X"]:
            return
        # dfs all four directions to cell current cell "O"
        board[r][c] = "*"
        Solution.dfs(r-1, c, board)
        Solution.dfs(r, c-1, board)
        Solution.dfs(r+1, c, board)
        Solution.dfs(r, c+1, board)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        for r in range(rows):
            for c in range(cols):
                # start from porders try to mark all non desired cells
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    Solution.dfs(r, c, board)

        # Capture surrounded regions (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # Uncapture unsurrounded regions (* -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "*":
                    board[r][c] = "O"
        return board


s = Solution()
print(s.solve(board=[["X", "X", "X", "X"], ["X", "O", "O", "X"], [
      "X", "X", "O", "X"], ["X", "O", "X", "X"]]))
