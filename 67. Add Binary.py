class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res=""
        a = a[::-1]
        b = b[::-1]

        if len(a) < len(b):
            a+="0"*(len(b) - len(a))
        else:
            b+="0"*(len(a) - len(b))

        for i in range(len(a)):
            total = int(a[i]) + int(b[i]) + carry
            res += str(total % 2)
            carry = total // 2

        if carry == 1:
            res += "1"        
        
        return res[::-1]
