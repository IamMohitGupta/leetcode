class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
        left = {'N':'W', 'W':'S', 'S':'E', 'E':'N'}
        
        obs = set()
        for i in obstacles:
            obs.add((i[0], i[1]))

        eud_dist = 0

        x = 0
        y = 0
        dirtn = 'N'
        for i in commands:
            if i>0:
                for j in range(i):
                    if dirtn == 'N':
                        if (x,y+1) not in obs:
                            y+=1
                        else:
                            break
                    elif dirtn == 'E':
                        if (x+1,y) not in obs:
                            x+=1
                        else:
                            break
                    elif dirtn == 'S':
                        if (x,y-1) not in obs:
                            y-=1
                        else:
                            break
                    else:
                        if (x-1,y) not in obs:
                            x-=1
                        else:
                            break
                    eud_dist = max(eud_dist, x**2 + y**2)
            else:
                if i == -2:
                    dirtn = left[dirtn]
                else:
                    dirtn = right[dirtn]
        return eud_dist

