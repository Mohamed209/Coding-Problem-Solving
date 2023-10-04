class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rev_invert(x: str) -> str:
            res = ""
            for char in x:
                if char == "0":
                    res += "1"
                else:
                    res += "0"
            return res[::-1]

        sn = "0"
        for i in range(2, n + 1):
            sn = sn + "1" + rev_invert(sn)
        return sn[k - 1]


s = Solution()
s.findKthBit(4, 11)
