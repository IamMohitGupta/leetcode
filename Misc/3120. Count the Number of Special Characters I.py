class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        m_lo = {}
        m_up = {}
        res=0

        for i in word:
            if i not in m_lo and i not in m_up:
                if i.islower():
                    m_lo[i] = 1
                else:
                    m_up[i] = 1
        for i in m_lo:
            if i.upper() in m_up:
                res+=1
        
        return res
