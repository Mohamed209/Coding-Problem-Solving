# https://www.geeksforgeeks.org/problems/print-diagonally4331/1
class Solution:
    def diagView(self, mat):
        # code here
        # the trick in this problem is at any diagonal i all indexes i,j sums to i
        # anti-diag0 -> 0,0
        # anti-diag1 -> 0,1 and 1,0
        # anti-diag2 -> 0,2 and 1,1 and 2,0
        # anti-diag3 -> 1,2 and 2,1
        # anti-diag4 -> 2,2
        # so we can loop through all the diagonals and print the elements in them
        res = [[] for _ in range(2 * len(mat) - 1)]
        n = len(mat)
        for i in range(n):
            for j in range(n):
                res[i + j].append(mat[i][j])
        return [elem for sublist in res for elem in sublist]


# Driver code
if __name__ == "__main__":
    s=Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(s.diagView(mat))
    mat = [[1, 2], [3, 4]]
    print(s.diagView(mat))
