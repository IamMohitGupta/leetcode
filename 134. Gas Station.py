class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost)<0:
            return -1
        else:
            tank=0
            idx = 0
            for i in range(len(gas)):
                tank += gas[i] - cost[i]
                if tank < 0:
                    idx = i + 1
                    tank = 0
            return idx

"""

Approach: 
Check if sum of gas - sum of cost is more than or less than 0, if less then no solution exists.
Else,
keep adding gas[i] - cost[i] in tank variable and if tank is less than 0, reset to 0

"""
