class Solution:
    def minElement(self, nums: List[int]) -> int:
        result = 10**5
        for i in nums:
            curr = 0
            while i:
                curr+=i%10
                i = i//10
            result = min(result, curr)
        return result
