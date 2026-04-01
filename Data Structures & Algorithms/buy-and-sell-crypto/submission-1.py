class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        checked = [prices[0]]
        max_profits = []
        for i, n in enumerate(prices):
            sell = n
            profit = sell - min(checked)
            checked.append(prices[i])
            max_profits.append(profit)

        if(max(max_profits) <= 0):
            return 0
        return max(max_profits)