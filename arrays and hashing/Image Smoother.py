# https://leetcode.com/problems/image-smoother/description
from typing import List
import math


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])
        res = [[0] * cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                valid_cells = 9  # 3*3 filter
                total_sum = img[r][c]
                eight_directions = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                for dr, dc in eight_directions:
                    if 0 <= r + dr < rows and 0 <= c + dc < cols:
                        total_sum += img[r + dr][c + dc]
                    else:
                        valid_cells -= 1
                res[r][c] = math.floor(total_sum / valid_cells)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.imageSmoother([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(s.imageSmoother([[100, 200, 100], [200, 50, 200], [100, 200, 100]]))
    print(
        s.imageSmoother([[2, 3, 4], [5, 6, 7], [8, 9, 10], [11, 12, 13], [14, 15, 16]])
    )
