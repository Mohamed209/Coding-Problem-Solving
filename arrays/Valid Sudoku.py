# https://leetcode.com/problems/valid-sudoku/
from typing import List
import numpy as np
from collections import Counter


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board = np.array(board)
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in board[i, j+1:] or board[i][j] in board[i+1:, j]:
                    return False
        # serach in every 3*3
        for k in range(3):
            for v in range(3):
                freq = Counter(board[k*3:k*3+3, v*3:v*3+3].flatten())
                for key in freq:
                    if key != '.' and freq[key] > 1:
                        return False
        return True
