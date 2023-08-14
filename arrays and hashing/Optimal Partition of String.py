# https://leetcode.com/problems/optimal-partition-of-string/description/
class Solution:
    def partitionString(self, s: str) -> int:
        ptr, cnt = 0, 0
        seen_before = set()  # current window seen before hash set
        while ptr < len(s):
            # greedy thinking , expand ptr as far as we can
            # until we hit duplicate
            if s[ptr] in seen_before:
                cnt += 1
                seen_before.clear()
            seen_before.add(s[ptr])
            ptr += 1
        return cnt + 1


s = Solution()
print(s.partitionString(s="abacaba"))
