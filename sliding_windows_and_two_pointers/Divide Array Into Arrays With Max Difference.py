# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/
from typing import List


class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        # Yield successive n-sized
        # chunks from l.
        def divide_chunks(l, n):
            # looping till length l
            for i in range(0, len(l), n):
                yield l[i : i + n]

        res = []
        chunks = divide_chunks(nums, 3)
        for chunk in chunks:
            if chunk[-1] - chunk[0] > k:
                return []
            res.append(chunk)
        return res


s = Solution()
print(
    s.divideArray(
        nums=[
            15,
            13,
            12,
            13,
            12,
            14,
            12,
            2,
            3,
            13,
            12,
            14,
            14,
            13,
            5,
            12,
            12,
            2,
            13,
            2,
            2,
        ],
        k=2,
    )
)
