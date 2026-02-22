class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(index, l):
            if index == len(nums):
                res.append(l.copy())
                return
            l.append(nums[index])
            dfs(index+1,l)
            l.pop()
            dfs(index+1, l)
        dfs(0,[])
        return res
            
