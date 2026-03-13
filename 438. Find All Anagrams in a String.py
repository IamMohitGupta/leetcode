class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if s==p:
            return [0]
        if len(p) > len(s):
            return []
        else:
            res=[]
            dp=[0]*26
            for i in p:
                dp[ord(i)-ord('a')]+=1
            l=1
            dp1=[0]*26
            for i in range(0,len(p)):
                dp1[ord(s[i])-ord('a')]+=1
            if dp==dp1:
                res.append(0)
            while l<=len(s)-len(p):
                dp1[ord(s[l-1])-ord('a')]-=1
                dp1[ord(s[l+len(p)-1])-ord('a')]+=1
                if dp==dp1:
                    res.append(l)
                l+=1

        return res
