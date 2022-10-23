# https://leetcode.com/problems/unique-paths/
class Solution:
    cache = {}

    def uniquePaths(self, m: int, n: int) -> int:
        # base cases
        if m == 0 or n == 0:
            return 0
        if m == 1 and n == 1:
            return 1
        # return cached paths if we found them before
        if ((m, n)) in Solution.cache:
            return Solution.cache[(m, n)]
        """
        we have only two options move right or down
        if we move down one cell , the problem is reduced to m-1,n , also for right the problem will be m,n-1
        then comes the role of recursion where we recursivly call the same function with the new grid cell size
        """
        ways = self.uniquePaths(m-1, n)+self.uniquePaths(m, n-1)
        Solution.cache[(m, n)] = ways
        return ways


s = Solution()
print(s.uniquePaths(3, 7))

# tabulation


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = []
        for _ in range(m+1):
            table.append([0]*(n+1))
        table[1][1] = 1
        for i in range(m+1):
            for j in range(n+1):
                if j+1 <= n:
                    table[i][j+1] += table[i][j]
                if i+1 <= m:
                    table[i+1][j] += table[i][j]
        return table[m][n]


s = Solution()
print(s.uniquePaths(3, 7))
