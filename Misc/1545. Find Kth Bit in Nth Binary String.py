class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invertBinary(s: str) -> str:
            return s.translate(str.maketrans('01', '10'))
        m = {0: "0"}
        for i in range(1,20):
            x = m[i-1]
            y = invertBinary(x)
            m[i] = x+"1"+y[::-1]
        
        return m[n-1][k-1]
