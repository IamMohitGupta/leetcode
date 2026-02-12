class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if len(nums) == 1:
            return [nums[0]]
        
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                m[nums[i]]+=1
            else:
                m[nums[i]] = 1

        l = []
        max_freq = max(m.values())
        for i in range(max_freq,0,-1):
            for key, value in m.items():
                if value == i:
                    l.append(key)
                    k -= 1
                    if k == 0:
                        return l
        return l
