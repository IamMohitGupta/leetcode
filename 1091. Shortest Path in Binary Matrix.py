class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] != 0 or grid[len(grid)-1][len(grid)-1]!=0:
            return -1
        n = len(grid)
        dp=[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0),  (1,1)]
        queue = deque([[0,0]])
        result=1
        while queue:
            size = len(queue)
            for i in range(size):
                x = queue.popleft()
                if (x[0], x[1]) == (n-1, n-1):
                    return result
                for i in dp:
                    x1 = x[0]+i[0]
                    y1 = x[1]+i[1]
                    if 0<= x1 <n and 0<=y1<n and grid[x1][y1] == 0:
                        grid[x1][y1] = 1
                        queue.append([x1,y1])
            result+=1
        return -1
