class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        m={}
        
        for i in range(len(nums)):
            if nums[i] in m:
                prev = m[nums[i]]
                curr = i
                if abs(prev-curr)<=k:
                    return True
                m[nums[i]] = i
            else:
                m[nums[i]] = i
        
        return False
