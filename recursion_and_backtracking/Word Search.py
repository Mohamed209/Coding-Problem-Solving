# https://leetcode.com/problems/word-search
from collections import Counter
from typing import List


class Solution:
    def __init__(self) -> None:
        self.cuurent_path = set()

    def dfs(self, r, c, word, board):
        # base case / dead end or dead start
        if (
            r < 0
            or r >= len(board)
            or c < 0
            or c >= len(board[0])
            or board[r][c] != word[0]
            or (r, c) in self.cuurent_path
        ):
            return False
        elif (
            len(word) == 1 and word[0] == board[r][c]
        ):  # base case when word is reduced to one character and current cell equal this character
            return True
        # dfs in 4 directions
        self.cuurent_path.add((r, c))
        res = (
            self.dfs(r, c + 1, word[1:], board)
            | self.dfs(r, c - 1, word[1:], board)
            | self.dfs(r + 1, c, word[1:], board)
            | self.dfs(r - 1, c, word[1:], board)
        )
        self.cuurent_path.remove((r, c))
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        word_count = Counter(word)
        board_count = Counter(
            "".join(["".join(row) for row in board])
        )  # flatten array to one string
        # Don't need to search if a certain character appears more often in word than in board
        for char in word:
            if word_count[char] > board_count[char]:
                return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(r, c, word, board):
                    return True
        return False


s = Solution()
print(
    s.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCCED",
    )
)
print(
    s.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="SEE",
    )
)
print(
    s.exist(
        board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        word="ABCB",
    )
)
