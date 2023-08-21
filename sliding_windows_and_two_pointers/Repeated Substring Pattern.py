# https://leetcode.com/problems/repeated-substring-pattern/description/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Yield successive n-sized
        # chunks from l.
        def divide_chunks(l, n):
            # looping till length l
            for i in range(0, len(l), n):
                yield l[i : i + n]

        mid = len(s) // 2
        while mid > 0:
            chuncks = [c for c in divide_chunks(s, mid)]
            print(chuncks)
            if all(chuncks[0] == ch for ch in chuncks):
                return True
            # need to try another partitions
            mid -= 1
        return False


s = Solution()
print(s.repeatedSubstringPattern(s="abcabcabcabc"))
