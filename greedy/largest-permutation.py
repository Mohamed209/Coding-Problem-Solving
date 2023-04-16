# https://www.interviewbit.com/problems/largest-permutation/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        idx_to_nums = {k: v for (v, k) in enumerate(A)}
        _max = len(A)
        i = 0
        while B and _max:
            # what is the max element ?
            # for sure it must be len(A) becasue integer array A of size N consisting of unique integers from 1 to N
            # and in next iterations is hould be len(A)-1 ,len(A)-2 , ...
            maxidx = idx_to_nums[_max]
            # now if the greatest element is in correct place , skip this iteraton and do not decrease the swaps
            if maxidx == i:
                i += 1
                _max -= 1
                continue
            else:
                # swap
                tmp = A[i]
                A[i] = A[maxidx]
                A[maxidx] = tmp
                # reflect the swap to idx_to_nums
                idx_to_nums[tmp], idx_to_nums[_max] = (
                    idx_to_nums[_max],
                    idx_to_nums[tmp],
                )
                i += 1
                B -= 1
                _max -= 1
        return A


s = Solution()
print(s.solve([1, 2], 2))
print(s.solve([1, 2, 3, 4], 1))
print(s.solve([3, 2, 1], 2))
print(s.solve([8, 2, 7, 4, 5, 6, 3, 1], 2))
