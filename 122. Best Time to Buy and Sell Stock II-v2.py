class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # we can either buy, sell or do nothing on ith day
        # we sell if it is profitable: previous buy < current price
        # we buy if price < previous bought price
        
        lastBuy, profit = -1, 0
        
        for price in prices:
            if lastBuy != -1 and lastBuy < price:  # we sell if it is profitable
                profit += price - lastBuy
                lastBuy = price
            elif lastBuy == -1 or lastBuy > price:
                lastBuy = price
        
        return profit
