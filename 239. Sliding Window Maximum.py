class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        l=0
        i=0
        res=[]
        while i < len(nums):
            while q and nums[q[-1]]<nums[i]:
                q.pop()
            q.append(i)

            if l > q[0]:
                q.popleft()
            
            if i+1 >=k:
                res.append(nums[q[0]])
                l+=1
            i+=1
        return res

"""

Approach: 
Use a deque to add/remove elements from both left and right. Keep popping elements shorter than current element in deque.
And append the current number then, in the list add q[0] element and pop from left, since window moves ahead.

"""
