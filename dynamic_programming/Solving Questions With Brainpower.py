# https://leetcode.com/problems/solving-questions-with-brainpower/
from typing import List


class Solution:
    def dfs(self, questions, cache, i):
        if i >= len(questions):  # if brainpower will continue after very long time
            return 0
        if i in cache:
            # if i am revisiting a solved path in the decesion tree
            return cache[i]
        # solve current question
        solve_branch = questions[i][0] + self.dfs(
            questions, cache, i + 1 + questions[i][1]
        )
        # skip question
        skip_branch = self.dfs(questions, cache, i + 1)
        best_option = max(solve_branch, skip_branch)
        cache[i] = best_option
        return best_option

    def mostPoints(self, questions: List[List[int]]) -> int:
        cache = {}
        return self.dfs(questions, cache, 0)


s = Solution()
cases = [
    [[21, 5], [92, 3], [74, 2], [39, 4], [58, 2], [5, 5], [49, 4], [65, 3]],
    [[3, 2], [4, 3], [4, 4], [2, 5]],
    [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]],
    [[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]],
]
for case in cases:
    print(s.mostPoints(questions=case))
