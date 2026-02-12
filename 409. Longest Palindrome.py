class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for i in range(len(s)):
            if s[i] in m:
                m[s[i]]+=1
            else:
                m[s[i]] = 1
        
        freq = m.values()
        hasodd = False
        count_odd = 0
        count = 0
        for i in freq:
            if i%2 ==0:
                count+=i
            else:
                hasodd = True
                count+=i-1

        return count+(1 if hasodd else 0)

"""

Remember, for odd frequencies, we can always used them by making them even ( by subtracting 1).
Add 1 if odd freq present so in order to keep one full odd frequency

"""
