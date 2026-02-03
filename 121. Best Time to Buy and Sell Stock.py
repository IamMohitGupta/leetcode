class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_seen = float('inf')
        profit = 0
        for i in range(len(prices)):
            min_seen = min(prices[i], min_seen)
            profit = max(profit, prices[i]-min_seen)
        
        return profit


"""

Approach:
Keep in mind, the max profit is min buy and max sell number in sequence.
To do so, keep track of min stock proce seen so far.
Calculate profit by subtracting current price with min stock price seen so far and always substitute profit with max value of this operation (prices[i] - min_seen)

Return profit

"""
