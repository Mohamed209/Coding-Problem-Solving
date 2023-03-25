# https://leetcode.com/problems/surrounded-regions/
from typing import List


class Solution:
    def __init__(self) -> None:
        self.visited = set()

    def dfs(self, r, c, board, reject_symbol, replace_symbol):
        # base cases to stop rcursive dfs
        if (
            r < 0
            or r >= len(board)
            or c < 0
            or c >= len(board[0])
            or board[r][c] == reject_symbol
            or (r, c) in self.visited
        ):
            return
        self.visited.add((r, c))
        # start 4 directions dfs
        self.dfs(r, c - 1, board, reject_symbol, replace_symbol)
        self.dfs(r, c + 1, board, reject_symbol, replace_symbol)
        self.dfs(r - 1, c, board, reject_symbol, replace_symbol)
        self.dfs(r + 1, c, board, reject_symbol, replace_symbol)
        board[r][c] = replace_symbol

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # first phase disable non surrounded regions
        ROWS = len(board)
        COLS = len(board[0])
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (
                    r in [0, ROWS - 1] or c in [0, COLS - 1]
                ):  # i am on the border and found "O" --> let us dfs and mark all non surrounded regions
                    self.dfs(r, c, board, reject_symbol="X", replace_symbol="T")
        # second phase is to find surrounded regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != "T":
                    self.dfs(r, c, board, reject_symbol="X", replace_symbol="X")
        # third phase just convert every "T" to "O"
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"


s = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "O", "X"],
    ["X", "X", "O", "X"],
    ["X", "O", "X", "X"],
]
s.solve(board)
print(board)
s = Solution()
board = [
    ["X", "X", "X", "X"],
    ["X", "O", "X", "X"],
    ["X", "O", "X", "X"],
    ["X", "O", "X", "X"],
]
s.solve(board)
print(board)
