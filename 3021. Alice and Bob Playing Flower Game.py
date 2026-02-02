class Solution(object):
    def flowerGame(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        
        lane1_odd  = (n + 1) // 2
        lane1_even = n // 2

        lane2_odd  = (m + 1) // 2
        lane2_even = m // 2

        return lane1_odd * lane2_even + lane1_even * lane2_odd

"""

Approach:
In order for alice to win, the sum of flowers on lane 1 and lane 2 should be odd.

"""
