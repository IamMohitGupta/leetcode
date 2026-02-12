class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        l = list(set(nums))
        l.sort()
        curr = l[0]
        maxs = 0
        count = 1

        for i in range(1,len(l)):
            if l[i] == curr + 1:
                count+=1
                maxs = max(maxs, count)
                curr = l[i]
                # print(count, maxs)
            else:
                curr = l[i]
                count = 1
        
        return max(maxs, count)
