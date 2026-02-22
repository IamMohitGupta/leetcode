class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def ways(n):
            if n<=1:
                return 1
            if n in memo:
                return memo[n]
            
            memo[n] = ways(n-1)+ways(n-2)
            return memo[n]
        
        return ways(n)

"""

Approach:
Simple recurssion, but use memoization.

"""
