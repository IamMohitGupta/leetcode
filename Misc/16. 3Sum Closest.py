class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3:
            return sum(nums)
        nums.sort()
        result=0
        temp=10**4+1
        m={}
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            x = nums[i]
            while l < r:
                res = x + nums[l] + nums[r]
                if abs(target - res) < temp:
                    temp = abs(target - res)
                    result = res
                if res < target:
                    l += 1
                elif res > target:
                    r -= 1
                else:
                    return target
        return result
