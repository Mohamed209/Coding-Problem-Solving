# https://www.interviewbit.com/problems/seats/
class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        xs = []
        total_cost = 0
        for i in range(len(A)):
            if A[i] == "x":
                xs.append(i)
        if xs == []:
            return 0
        xs = [(x - i) for i, x in enumerate(xs)]
        # The number of jumps always be minimum when we shift points to the median
        midpoint = xs[len(xs) // 2]
        # let us find the cost of moving every x to the midpoint
        for x in xs:
            total_cost += abs(x - midpoint)
            total_cost %= 1e7 + 3
        return int(total_cost)


s = Solution()
print(s.seats("....x..xx...x.."))
