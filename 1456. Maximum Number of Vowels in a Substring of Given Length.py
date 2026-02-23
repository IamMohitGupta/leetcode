class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels=set('aeiou')
        count = 0
        res=0
        l=0
        r=0
        while r<len(s):
            if s[r] in vowels:
                count+=1
            if r-l+1 == k:
                res = max(res, count)
                if res == k:
                    return res
                if s[l] in vowels:
                    count-=1
                l+=1
            r+=1
        return res

"""
Sliding window
"""
