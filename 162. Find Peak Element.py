class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if (mid > 0 and nums[mid-1]>nums[mid]):
                right = mid-1
            elif (mid < len(nums)-1 and nums[mid+1]>nums[mid]):
                left = mid+1
            else:
                return mid

"""

O(logn) - Think of binary search
Peak = Greater than its neighbors

"""
