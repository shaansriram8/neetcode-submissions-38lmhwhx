class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1 #l = buy, r = sell
        max_profit = 0
        while r < len(prices):
            profit = prices[r] - prices[l] #curr profit
            if prices[r] < prices[l]: #if we find a better buy date
                l = r
            max_profit = max(profit, max_profit)
            r+=1
        return max_profit


        
      