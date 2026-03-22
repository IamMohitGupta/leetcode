class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        first = 0
        linear_sum = 0
        maxsum = float('-inf')
        for i in range(len(nums)):
            first+=(i*nums[i])
            linear_sum+=nums[i]
        maxsum = max(first,maxsum)
        for i in range(len(nums)-1,-1,-1):
            first+=linear_sum-(len(nums)*nums[i])
            maxsum = max(first,maxsum)
        return maxsum

