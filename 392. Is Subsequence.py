class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t)<len(s):
            return False
        l = 0
        for i in s:
            found = False
            for j in range(l, len(t)):
                if t[j] == i:
                    l = j+1
                    found = True
                    break
            if not found:
                return False
        return True
