class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n==0:
            return 1
        
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result


"""

Keep in mind, this a binary exponentiation problem:

x^n = (x^2)^n/2

If n is odd: x^n = x * x^n-1

"""
        
