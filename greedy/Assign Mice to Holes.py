# https://www.interviewbit.com/problems/assign-mice-to-holes/
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A.sort()
        B.sort()
        minutes = []
        for mouse, hole in zip(A, B):
            minutes.append(
                abs(mouse - hole)
            )  # distance between the mouse and its nearest hole
        return max(minutes)


s = Solution()
print(s.mice([-4, 2, 3], [0, -2, 4]))
