class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set(["a", "A", "e", "E", "i", "I", "O", "o", "u", "U"])
        vowels_str = []
        for char in s:
            if char in vowels:
                vowels_str.append(char)
        vowels_str = vowels_str[::-1]
        s = [c for c in s]
        j = 0
        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowels_str[j]
                j += 1
        return "".join([c for c in s])
