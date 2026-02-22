class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words.sort()
        m={}
        for i in words:
            if i in m:
                m[i]+=1
            else:
                m[i] = 1
        l=[]
        sorted_m = sorted(m.items(), key = lambda x:(-x[1], x[0]))

        for key, value in sorted_m:
            if k==0:
                return l
            else:
                l.append(key)
                k-=1
        return l
