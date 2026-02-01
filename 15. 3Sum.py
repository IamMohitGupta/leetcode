class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        l=[]
        for i in range(len(nums)-2):
            res=[]
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left]+nums[right] == -nums[i]:
                    res.append(nums[i])
                    res.append(nums[left])
                    res.append(nums[right])
                    l.append(res)
                    res=[]
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left]+nums[right] > -nums[i]:
                    right-=1
                else:
                    left+=1
        return l


"""

Approach:
Fix one number, and try to use 2sum approach (find two numbers after the fixed number who sum is equal to negative current sum)
basically b+c = -a

No need to use hashmap approach as in 2sum question, since the numbers are being sorted. Can use 2 pointer approach. 

PS: Remeber to skip the duplicates

"""
