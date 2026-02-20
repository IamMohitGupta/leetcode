class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        m={}
        count = 1
        l = 0
        r = 0
        while r<len(s):
            if s[r] in m:
                l = max(l, m[s[r]] + 1)
            m[s[r]] = r
            count = max(count, r - l + 1)
            r+=1
        return count

"""

Approach:
Just keep track of indices with r pointer and length would be r-l+1 of the substring.
If duplicate found that is it is present in map, then l = maz(l, duplicate previous index + 1)

"""
