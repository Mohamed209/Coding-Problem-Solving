# https://leetcode.com/problems/permutation-in-string/
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        s1_freq = Counter(s1)
        for i in range(len(s2) - window_size + 1):
            current_window = s2[i : i + window_size]
            if i == 0:
                current_window_freq = Counter(current_window)
                if current_window_freq == s1_freq:
                    return True
            else:
                # optimized solution , no need to compute the frequency dict for every window
                # we can build on top of previous computed windows
                current_window_freq[s2[i - 1]] -= 1
                if current_window_freq[s2[i - 1]] <= 0:
                    del current_window_freq[s2[i - 1]]
                if current_window[-1] in current_window_freq:
                    current_window_freq[current_window[-1]] += 1
                else:
                    current_window_freq[current_window[-1]] = 1
                if current_window_freq == s1_freq:
                    return True
        return False


s = Solution()
print(s.checkInclusion(s2="ooolleoooleh", s1="hello"))
print(s.checkInclusion(s1="ab", s2="eidbaooo"))
print(s.checkInclusion(s1="ab", s2="eidboaoo"))
