class Solution:
    def minOperations(self, n: int) -> int:
        arr = [0]*31
        for i in range(31):
            arr[i] = pow(2,i)
        print(arr)

        count = 0
        while n!=0:
            for i in range(len(arr)):
                if arr[i]>n:
                    n = min(arr[i]-n,abs(arr[i-1]-n))
                    count+=1
                    break
        return count


"""

Approach:
Always get closer to a power of 2, thats it

"""

