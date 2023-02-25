# https://leetcode.com/problems/flood-fill
from typing import List


class Solution:
    def dfs(self, image, sr, sc, target_color, start_cell_color):
        # base case if i am out of bounds
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return image
        # another base case If i landed in a visited cell
        elif image[sr][sc] == target_color:
            return image
        # another base case , if current pixel color is not equal the starting pixel color
        elif image[sr][sc] != start_cell_color:
            return image
        # paint current position
        image[sr][sc] = target_color
        # recursively paint pixels connected 4-directionally to current position
        self.dfs(image, sr-1, sc, target_color, start_cell_color)
        self.dfs(image, sr+1, sc, target_color, start_cell_color)
        self.dfs(image, sr, sc-1, target_color, start_cell_color)
        self.dfs(image, sr, sc+1, target_color, start_cell_color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.dfs(image, sr, sc, color, image[sr][sc])
        return image


s = Solution()
print(s.floodFill(image=[[1, 1, 1], [1, 1, 0],
      [1, 0, 1]], sr=1, sc=1, color=2))
print(s.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=1, sc=0, color=2))
print(s.floodFill(image=[[0, 0, 0], [0, 0, 0]], sr=1, sc=0, color=0))
