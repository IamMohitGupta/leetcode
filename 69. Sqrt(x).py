class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x<2:
            return x
        
        l = 1
        r = x // 2
        ans=0
        while l<=r:
            mid = (l+r)// 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                r = mid-1
            elif mid*mid < x:
                ans = mid
                l = mid+1
        return ans
