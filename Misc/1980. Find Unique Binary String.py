class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        nums.sort()
        print(nums)
        def bintoint(s:str):
            s=s[::-1]
            res=0
            for i in range(len(s)):
                if s[i] == '1':
                    res+=2**i
            return res

        l=[]
        res=""
        length = len(nums[0])

        for i in range(2**len(nums)):
            if i==len(nums):
                res = bin(i)[2:]
                res = '0'*(length - len(res))+res
                break
            else:
                if bintoint(nums[i]) !=i:
                    res = bin(i)[2:]
                    res = '0'*(length - len(res))+res
                    break
       
        return res
