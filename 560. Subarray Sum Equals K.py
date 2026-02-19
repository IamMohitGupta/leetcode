class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curr_sum = 0
        count = 0
        prefix_freq = {0:1}

        for i in nums:
            curr_sum+=i

            if curr_sum-k in prefix_freq:
                count+=prefix_freq[curr_sum-k]
            
            if curr_sum in prefix_freq:
                prefix_freq[curr_sum]+=1
            else:
                prefix_freq[curr_sum] = 1
        return count
