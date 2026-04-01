class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        max_profit = 0

        while r < len(prices):
            profit = prices[r]-prices[l]
            if prices[l] > prices[r]:
                r = l
                l+=1
            r+=1
            max_profit = max(profit, max_profit)
        return max_profit
        