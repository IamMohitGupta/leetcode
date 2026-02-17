class Solution:
    def minimumDeletions(self, s: str) -> int:
        countb = 0
        res=0
        for i in s:
            if i == 'a' and countb >0:
                res+=1
                countb-=1
            if i=='b':
                countb+=1
        return res

"""

Approach:
The goal is not have a sequence of 'ba' ever in the string as we parse from left to right

Ex: bbaabb
count b-> 1 2 (encounter a and count b > 0, subtract count b by 1 and add 1 to the result). And so on.

"""
