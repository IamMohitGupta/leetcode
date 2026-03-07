class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s)<4 or len(s)>12:
            return []
        l = []
        def backtrack(i,dots,curIP):
            if i == len(s) and dots == 4:
                l.append(curIP[:-1])
                return
            if dots == 4:
                return
            for j in range(i, min(i+3, len(s))):
                if s[i] == '0' and j > i:
                    break
                if int(s[i:j+1]) < 256:
                    backtrack(j+1, dots+1, curIP+s[i:j+1]+".")
        backtrack(0,0,"")
        return l
