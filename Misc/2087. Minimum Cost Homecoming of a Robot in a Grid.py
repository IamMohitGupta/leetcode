class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        
        cost = 0
        if startPos[0] < homePos[0]:
            for i in range(startPos[0]+1, homePos[0]+1):
                cost+=rowCosts[i]
        else:
            for i in range(startPos[0]-1, homePos[0]-1, -1):
                cost+=rowCosts[i]
        

        if startPos[1] < homePos[1]:
            for i in range(startPos[1]+1, homePos[1]+1):
                cost+=colCosts[i]
        else:
            for i in range(startPos[1]-1, homePos[1]-1, -1):
                cost+=colCosts[i]
        
        return cost
