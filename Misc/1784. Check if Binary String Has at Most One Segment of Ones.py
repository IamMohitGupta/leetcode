class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 1 and s[0] == '1':
            return True
        found0 = False
        for i in range(1,len(s)):
            if s[i] == '1' and found0:
                return False
            if s[i] == '0':
                found0 = True
        return True
