class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def rec(remaining, numlist, i):
            if remaining == 0:
                res.append(numlist.copy())
                return
            elif remaining < 0 or i >= len(candidates):
                return
            else:
                numlist.append(candidates[i])
                rec(remaining-candidates[i], numlist, i+1)
                numlist.pop()

                current = candidates[i]

                while i<len(candidates) and candidates[i]==current:
                    i+=1
                
                rec(remaining, numlist, i)

        rec(target, [], 0)
        return res
