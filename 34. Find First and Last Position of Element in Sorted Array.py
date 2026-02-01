class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        l=[]
        if target not in nums:
            return [-1,-1]
        else:
            for i in range(len(nums)):
                if nums[i]==target and len(l) == 0:
                    l.append(i)
                if nums[i] > target and len(l) == 1:
                    l.append(i - 1)
                    return l
        if len(l) == 1:
            l.append(len(nums)-1)
        return l
        
