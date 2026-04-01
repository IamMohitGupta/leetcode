class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        robots = []

        for i in range(len(positions)):
            robots.append([positions[i], healths[i], directions[i], i])
        robots.sort(key = lambda x:x[0])

        stack = []

        for robot in robots:
            curr = robot

            while stack and stack[-1][2] == 'R' and curr[2] == 'L':
                top = stack[-1]
                if top[1] > curr[1]:
                    top[1]-=1
                    curr[1] = 0
                    break
                elif top[1] == curr[1]:
                    curr[1] = 0
                    stack.pop()
                    break
                else:
                    curr[1]-=1
                    top[1] = 0
                    stack.pop()
            if curr[1]>0:
                stack.append(curr)
        
        res=[]
        for i in stack:
            res.append((i[3], i[1]))
        res.sort()
        result = []
        for i,j in res:
            result.append(j)
        return result
        
