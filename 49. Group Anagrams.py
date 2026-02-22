class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dp = [0]*26
        m={}
        for i in strs:
            for j in i:
                dp[ord(j)-ord('a')] +=1
            key = tuple(dp)
            if key in m:
                m[key].append(i)
            else:
                m[key] = [i]
            dp = [0]*26
        l=[]
        for key,value in m.items():
            l.append(value)
        return l
