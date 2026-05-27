class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        m_lower = {}
        m_upper = {}
        for i in range(len(word)-1,-1,-1):
            if word[i].islower() and word[i] not in m_lower:
                m_lower[word[i]] = i
        
        for i in range(len(word)):
            if word[i].isupper() and word[i] not in m_upper:
                m_upper[word[i]] = i
        
        res = 0

        for i in m_lower:
            if i.upper() in m_upper:
                if m_lower[i] < m_upper[i.upper()]:
                    res+=1
        return res
