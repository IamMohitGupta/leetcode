class Solution:
    def countBits(self, n: int) -> List[int]:
        if n== 0:
            return [0]
        elif n==1:
            return [0,1]
        else:
            res=[0,1]
            x = 1
            temp=1
            for i in range(2,n+1):
                if i == x*2:
                    x = x*2
                    res.append(1)
                else:
                    y = i-x
                    res.append(res[y]+res[x])   
            return res
