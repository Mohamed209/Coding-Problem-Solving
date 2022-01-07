# https://leetcode.com/problems/flood-fill/
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        self.fill(image, sr, sc, newColor, image[sr][sc])
        return image

    def fill(self, image, sr, sc, newColor, oldColor):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or oldColor != image[sr][sc]:
            return
        image[sr][sc] = newColor
        self.fill(image, sr+1, sc, newColor, oldColor)
        self.fill(image, sr-1, sc, newColor, oldColor)
        self.fill(image, sr, sc+1, newColor, oldColor)
        self.fill(image, sr, sc-1, newColor, oldColor)
