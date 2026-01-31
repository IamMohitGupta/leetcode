class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1
        maxarea = 0
        while left<right:
            area = min(height[left],height[right])*(right-left)
            maxarea = max(maxarea,area)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return maxarea

"""

Approach:

2 pointer: 
Initial left pointer at position 0
Initial right pointer at the end of height list

Maximum area can be min height of left and right pointed x the width between them.
Assuming maxarea to be 0 initially, change maxarea to be maximum of above calculated area and maxarea

If height of left pointer is smaller than right pointer then move left pointer up by 1, else decrease right pointer by 1

"""
