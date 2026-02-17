class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return "1"
        else:
            def newString(s: str) -> str:
                count = 1
                res=""
                for i in range(len(s)-1):
                    if s[i] == s[i+1]:
                        count+=1
                    else:
                        res+=str(count)+s[i]
                        count = 1
                res += str(count) + s[-1]
                return res

            l=["1"]
            for i in range(n-1):
                res = newString(l[-1])
                l.append(res)
            
        return(l[-1])
