class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        lengtha = len(a)
        lengthb = len(b)
        aidx = []
        bidx = []
        right = lengtha-1
        curra = s[0:lengtha]
        currb = s[0:lengthb]
        if curra == a:
            aidx.append(0)
        if currb == b:
            bidx.append(0)
        for i in range(1, len(s) - lengtha + 1):
            curra = curra[1:] + s[i + lengtha - 1]
            if curra == a:
                aidx.append(i)

        for i in range(1, len(s) - lengthb + 1):
            currb = currb[1:] + s[i + lengthb - 1]
            if currb == b:
                bidx.append(i)

        res = []
        j = 0

        for i in aidx:
            while j < len(bidx) and bidx[j] < i - k:
                j += 1
            
            if j < len(bidx) and abs(bidx[j] - i) <= k and i>=0:
                res.append(i)
        return res

