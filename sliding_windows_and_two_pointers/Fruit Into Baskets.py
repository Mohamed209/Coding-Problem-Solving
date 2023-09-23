# https://leetcode.com/problems/fruit-into-baskets/description/
import collections
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = collections.defaultdict(int)
        left, right, current_count, res = 0, 0, 0, 0
        while right < len(fruits):
            baskets[fruits[right]] += 1
            current_count += 1
            while len(baskets) > 2:
                baskets[fruits[left]] -= 1
                current_count -= 1
                left += 1
                if not baskets[fruits[left]]:
                    baskets.pop(fruits[left])
            res = max(res, current_count)
            right += 1
        return res


s = Solution()
s.totalFruit([1, 2, 1])
