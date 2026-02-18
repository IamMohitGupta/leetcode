class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        x = n&1
        while n>0:
            n = n >> 1
            if n&1 ==x:
                return False
            x = n&1
        return True

"""

Keep doing right shift, and check the right most bit. If same as previous return false

"""
