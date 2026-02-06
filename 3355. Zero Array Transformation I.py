class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        l=[0]*(len(nums)+1)
        for a,b in queries:
            l[a] += -1
            l[b+1] += 1

        for i in range(1,len(l)):
            l[i] = l[i]+l[i-1]
        

        l = l[0:len(nums)]

        for i in range(len(nums)):
            nums[i] += l[i]
            if nums[i] > 0:
                return False  
        return True

"""

Approach:
Create another array with size 1 greater than nums
For ranges a,b: Just add -1 at position a and +1 and position b+1
Just calculate prefix sum and add it to the main array. If sum ==0 return True, else False

"""
