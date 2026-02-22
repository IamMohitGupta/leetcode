class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(i, remain, path):
            if remain == 0:
                res.append(path.copy())
                return
            if remain < 0 or i == len(candidates):
                return

            path.append(candidates[i])
            dfs(i, remain-candidates[i], path)
            path.pop()
            dfs(i+1, remain, path)
        dfs(0,target, [])
        return res

"""

Recurrsive approach: Take an elemnent or dont take

"""
