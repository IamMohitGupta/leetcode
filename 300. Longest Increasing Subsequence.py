class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        maximum = 0
        for i in range(len(nums)):
            res=0
            for j in range(i):
                if nums[j]<nums[i]:
                    res = max(res, dp[j])
            dp[i] = res+1
            maximum = max(maximum, dp[i])
        return maximum

"""

Approach: Keep maximum length of increasing subsequence at a particular index.

"""
