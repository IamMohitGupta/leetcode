class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def checkpalindrome(s, a, b):
            left = a
            right = b
            while left<right:
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False
            return True


        left = 0
        right = len(s)-1

        while left < right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                a = checkpalindrome(s,left+1,right)
                b = checkpalindrome(s,left,right-1)
                return a or b
        return True

"""

Approach: Check palindrome, if a mismatch occurs:
1. Increase left by 1 and check the substring is a palindrome or nor
2. Or Reduce right by 1 and check plaindrome.

If either is true return true

"""
