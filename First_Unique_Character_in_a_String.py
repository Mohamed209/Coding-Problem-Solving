class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}  # map to count occurance O(n)
        for char in s:
            if char in freq:
                freq[char] = freq[char]+1
            else:
                freq[char] = 1
        # find first elem with ocurance 1 O(n)
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1


s = Solution()
print(s.firstUniqChar("dddccdbba"))
