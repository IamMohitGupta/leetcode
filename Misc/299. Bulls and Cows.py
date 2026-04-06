class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        m_secret = {}
        s = set()
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls+=1
                s.add(i)
            else:
                if secret[i] in m_secret:
                    m_secret[secret[i]]+=1
                else:
                    m_secret[secret[i]] = 1

        cows = 0
        for i in range(len(guess)):
            if i not in s:
                if guess[i] in m_secret and m_secret[guess[i]]!=0:
                    m_secret[guess[i]]-=1
                    cows+=1
        

        return str(bulls)+"A"+str(cows)+"B"
        
