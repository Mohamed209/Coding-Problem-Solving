# https://leetcode.com/problems/maximum-score-after-splitting-a-string
class Solution:
    def maxScore(self, s: str) -> int:
        zeros_count = 0
        ones_count = s.count("1")
        max_score = 0
        for i in range(len(s) - 1):
            if s[i] == "0":
                zeros_count += 1
            else:
                ones_count -= 1
            max_score = max(max_score, zeros_count + ones_count)
        return max_score


if __name__ == "__main__":
    s = Solution()
    print(s.maxScore("011101"))
    print(s.maxScore("00111"))
    print(s.maxScore("1111"))
