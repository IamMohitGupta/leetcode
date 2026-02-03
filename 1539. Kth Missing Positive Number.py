class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        maxinlist = arr[-1]
        length = len(arr)
        if length == maxinlist:
            return maxinlist+k
        else:
            for i in range(1,maxinlist):
                if i not in arr:
                    k-=1
                    if k==0:
                        return i
                if i == maxinlist-1 and k!=0:
                    print(maxinlist+k)
                    return maxinlist+k
