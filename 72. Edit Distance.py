class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        def dfs(i,j):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if (i,j) in memo:
                return memo[(i,j)]
            if word1[i] == word2[j]:
                memo[(i,j)] = dfs(i-1,j-1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = 1+min(dfs(i-1,j), dfs(i,j-1), dfs(i-1,j-1))
                return memo[(i,j)]
        
        x = dfs(len(word1)-1, len(word2)-1)
        return x
