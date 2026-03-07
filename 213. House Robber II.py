class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return max(nums)
        l = [nums[0], max(nums[0], nums[1])]
        for i in range(2,len(nums)-1):
            curr = max(nums[i]+l[i-2], l[i-1])
            l.append(curr)
        firstmax = max(l[-1], l[-2])

        l = [nums[1], max(nums[1], nums[2])]
        for i in range(3,len(nums)):
            curr = max(nums[i]+l[i-2-1], l[i-1-1])
            l.append(curr)
        return max(firstmax, l[-1], l[-2])
