class Solution:
    def bitwiseComplement(self, n: int) -> int:
        x = bin(n)
        x = x[2:]
        x = x[::-1]
        print(x)
        res=0
        for i in range(len(x)):
            if x[i] == '0':
                res+=2**i
        return res
