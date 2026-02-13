class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count+=1
            else:
                if count ==1:
                    return nums[i]
                else:
                    count = 1
        return nums[-1]
