class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        max_len = 1
        m = {}
        l = 0
        i=0
        max_freq = 0

        while i<len(nums):
            m[nums[i]] = m.get(nums[i], 0)+1
            max_freq = max(max_freq, m[nums[i]])
            while i-l+1-max_freq>k:
                m[nums[l]]-=1
                l+=1
            max_len = max(max_len, max_freq)
            i+=1
        return max_len
