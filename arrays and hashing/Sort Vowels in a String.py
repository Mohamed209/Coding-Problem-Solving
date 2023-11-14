# https://leetcode.com/problems/sort-vowels-in-a-string/description/
class Solution:
    def sortVowels(self, s: str) -> str:
        res = ["#"] * len(s)
        vowels = {"a", "A", "e", "E", "i", "I", "o", "O", "u", "U"}
        found_vowels = []
        for i in range(len(s)):
            if s[i] not in vowels:
                res[i] = s[i]
            else:
                found_vowels.append(s[i])
        found_vowels.sort(reverse=True)
        for i in range(len(res)):
            if res[i] == "#":
                res[i] = found_vowels.pop()
        return "".join(c for c in res)


s = Solution()
print(s.sortVowels(s="lEetcOde"))
