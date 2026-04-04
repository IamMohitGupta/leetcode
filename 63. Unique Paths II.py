class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = {}
        def dfs(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return 0

            if obstacleGrid[i][j] == 1:
                return 0
            
            elif i == m-1 and j == n-1:
                return 1
            
            elif (i,j) in memo:
                return memo[(i,j)]

            else:
                memo[(i,j)] = dfs(i,j+1)+dfs(i+1,j)
                return memo[(i,j)]
        dist = dfs(0,0)
        return dist
