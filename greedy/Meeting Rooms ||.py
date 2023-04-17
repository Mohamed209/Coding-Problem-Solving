# https://www.interviewbit.com/problems/meeting-rooms/
class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        aux = []
        for interval in A:
            aux.append((interval[0], "s"))
            aux.append((interval[1], "e"))
        aux.sort()
        utilized_rooms = 0
        maxnedded = 0
        for au in aux:
            if au[1] == "s":
                utilized_rooms += 1
                if utilized_rooms > maxnedded:
                    maxnedded = utilized_rooms
            else:
                utilized_rooms -= 1
        return maxnedded


s = Solution()
As = [
    [[1, 18], [18, 23], [15, 29], [4, 15], [2, 11], [5, 13]],
    [[0, 30], [5, 10], [15, 20]],
    [[0, 30], [5, 10], [10, 15]],
    [(2, 7)],
    [[17, 26], [14, 22], [7, 29], [2, 29], [11, 14], [5, 24], [1, 14], [13, 14]],
]
for A in As:
    print(s.solve(A))
