from typing import List

import numpy as np


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_sets = [set() for _ in range(9)]
        cols_sets = [set() for _ in range(9)]
        board = np.array(board)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rows_sets[i] or board[i][j] in cols_sets[j]:
                        return False
                    else:
                        rows_sets[i].add(board[i][j])
                        cols_sets[j].add(board[i][j])
        # serach in every 3*3
        grid_set = set()
        for k in range(3):
            for v in range(3):
                grid = board[k * 3 : k * 3 + 3, v * 3 : v * 3 + 3].flatten()
                for num in grid:
                    if num != ".":
                        if num in grid_set:
                            return False
                        else:
                            grid_set.add(num)
                grid_set.clear()
        return True
